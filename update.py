import datetime as dt
import html
import json
import pathlib
import re
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent
HEADERS = {'User-Agent': 'SecurityWatchPersonal/2.0 (+GitHub Actions)', 'Accept': 'application/json, application/xml, application/rss+xml, */*'}
JST = dt.timezone(dt.timedelta(hours=9))
CISA_URL = 'https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json'
# JVN本体の公開RSS。JVN iPediaの旧URLは移行に伴い利用不可の場合があります。
JVN_FEEDS = ['https://jvn.jp/rss/jvn.rdf', 'https://jvn.jp/rss/jvn_new.rdf']
TERMS = ('microsoft', 'windows', 'uipath', 'chrome', 'edge', 'gitlab', 'office', 'sharepoint')


def fetch(url):
    last = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as res:
                return res.read()
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last = exc
            if attempt < 2:
                time.sleep(2 * (attempt + 1))
    raise RuntimeError(f'{url}: {last}')


def clean(value):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html.unescape(str(value or '')))).strip()


def parse_jvn(data):
    root = ET.fromstring(data)
    found = []
    for el in root.iter():
        if el.tag.split('}')[-1] != 'item':
            continue
        fields = {x.tag.split('}')[-1]: clean(x.text) for x in el}
        title, link = fields.get('title', ''), fields.get('link', '')
        if not title or not link.startswith('https://jvn.jp/'):
            continue
        found.append({'source': 'JVN', 'date': fields.get('date', '')[:10],
                      'title': title, 'description': fields.get('description', ''),
                      'action': '公式の対策情報を確認してください。', 'url': link,
                      'cve': '', 'priority': '要確認',
                      'search': (title + ' ' + fields.get('description', '')).lower()})
        if len(found) >= 40:
            break
    return found


def main():
    items, warnings = [], []
    status = {'CISA KEV': '取得失敗', 'JVN': '取得失敗'}
    try:
        raw = json.loads(fetch(CISA_URL))
        for v in sorted(raw.get('vulnerabilities', []), key=lambda x: x.get('dateAdded', ''), reverse=True)[:35]:
            cve = clean(v.get('cveID'))
            vendor, product = clean(v.get('vendorProject')), clean(v.get('product'))
            items.append({'source': 'CISA KEV', 'date': v.get('dateAdded', ''),
                          'title': f'{vendor} {product} — {cve}',
                          'description': clean(v.get('shortDescription')),
                          'action': clean(v.get('requiredAction')),
                          'url': 'https://www.cisa.gov/known-exploited-vulnerabilities-catalog',
                          'cve': cve, 'priority': '緊急（悪用確認）',
                          'search': f'{vendor} {product} {cve}'.lower()})
        status['CISA KEV'] = f"取得成功（{sum(x['source']=='CISA KEV' for x in items)}件）"
    except Exception as exc:
        warnings.append(f'CISA KEV取得失敗: {exc}')

    for url in JVN_FEEDS:
        try:
            jvn = parse_jvn(fetch(url))
            if jvn:
                items.extend(jvn)
                status['JVN'] = f'取得成功（{len(jvn)}件）'
                break
            warnings.append(f'JVN: {url} から記事を取得できませんでした')
        except Exception as exc:
            warnings.append(f'JVN取得失敗: {exc}')

    items.sort(key=lambda x: x['date'], reverse=True)
    payload = {'updated': dt.datetime.now(JST).strftime('%Y-%m-%d %H:%M JST'),
               'items': items, 'warnings': warnings, 'status': status}
    (ROOT / 'data.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    print('取得結果:', status)
    for warning in warnings:
        print('注意:', warning)
    if not items:
        raise RuntimeError('両方のデータソースから情報を取得できませんでした')


if __name__ == '__main__':
    main()
