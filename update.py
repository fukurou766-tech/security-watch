import json, urllib.request, datetime, pathlib, html, re
from xml.etree import ElementTree as ET
ROOT=pathlib.Path(__file__).parent
HEAD={'User-Agent':'SecurityWatchPersonal/1.0'}
def get(url):
    req=urllib.request.Request(url,headers=HEAD)
    with urllib.request.urlopen(req,timeout=35) as r:return r.read()
def clean(s):return re.sub(r'\s+',' ',re.sub(r'<[^>]*>','',html.unescape(str(s or '')))).strip()
now=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
items=[]; errors=[]
try:
    data=json.loads(get('https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json'))
    for v in sorted(data['vulnerabilities'],key=lambda x:x.get('dateAdded',''),reverse=True)[:35]:
        cve=v.get('cveID',''); vendor=clean(v.get('vendorProject')); product=clean(v.get('product'))
        items.append(dict(source='CISA KEV',date=v.get('dateAdded',''),title=f'{vendor} {product} — {cve}',description=clean(v.get('shortDescription')),action=clean(v.get('requiredAction')),url='https://www.cisa.gov/known-exploited-vulnerabilities-catalog',cve=cve,priority='緊急（悪用確認）',search=(vendor+' '+product+' '+cve).lower()))
except Exception as e:errors.append('CISA KEV: '+str(e))
# JVN RSS, Japanese titles and descriptions
for feed in ['https://jvndb.jvn.jp/ja/rss/jvndb_new.rdf','https://jvndb.jvn.jp/ja/rss/jvndb.rdf']:
    try:
        root=ET.fromstring(get(feed)); found=0
        for el in root.iter():
            if el.tag.split('}')[-1]!='item':continue
            fields={x.tag.split('}')[-1]:clean(x.text) for x in el}
            title=fields.get('title',''); link=fields.get('link','')
            if not title or not link:continue
            date=fields.get('date','')[:10]
            items.append(dict(source='JVN iPedia',date=date,title=title,description=fields.get('description',''),action='公式情報を確認してください',url=link,cve='',priority='要確認',search=(title+' '+fields.get('description','')).lower()))
            found+=1
            if found>=40:break
        if found:break
    except Exception as e:errors.append('JVN: '+str(e))
else:errors.append('JVN: RSSを取得できませんでした')
items.sort(key=lambda x:x['date'],reverse=True)
(ROOT/'data.json').write_text(json.dumps({'updated':now.strftime('%Y-%m-%d %H:%M JST'),'items':items,'errors':errors},ensure_ascii=False,indent=2),encoding='utf-8')
print('records',len(items),'errors',errors)
