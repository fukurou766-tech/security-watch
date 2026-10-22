import json
import os
import pathlib
import re
import time

ROOT = pathlib.Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'data.json').read_text(encoding='utf-8'))
CACHE_FILE = ROOT / 'translation_cache.json'
CACHE = json.loads(CACHE_FILE.read_text(encoding='utf-8')) if CACHE_FILE.exists() else {}
TERMS = ('microsoft', 'windows', 'uipath', 'chrome', 'edge', 'gitlab', 'office', 'sharepoint')

try:
    from deep_translator import GoogleTranslator
    translator = GoogleTranslator(source='en', target='ja')
except Exception as exc:
    translator = None
    print('翻訳機能の初期化失敗:', exc)

failed = 0
translated = 0


def ja(text):
    global failed, translated
    text = str(text or '').strip()
    if not text:
        return '記載なし', True
    if text in CACHE:
        return CACHE[text], True
    if translator is None:
        failed += 1
        return text, False
    try:
        # 非公式の無料翻訳サービス。長文は分割する。
        chunks = [text[i:i+2500] for i in range(0, len(text), 2500)]
        out = []
        for chunk in chunks:
            value = translator.translate(chunk)
            if not value:
                raise ValueError('翻訳結果が空です')
            out.append(value)
            time.sleep(0.4)
        result = ''.join(out)
        CACHE[text] = result
        translated += 1
        return result, True
    except Exception as exc:
        failed += 1
        print('翻訳失敗:', type(exc).__name__, str(exc)[:180])
        return text, False


def safe(text):
    return str(text).replace('\r', ' ').replace('\n', ' ').replace('<', '&lt;')


rows = ['# 🛡️ 脆弱性情報ダッシュボード', '',
        f"**最終取得：{DATA['updated']}**", '',
        f"**取得件数：{len(DATA['items'])}件**（CISA直近35件・JVN最大40件）", '',
        '> ※CISA KEVは「悪用確認済み」の一覧です。掲載製品が自分の環境に影響するかは、バージョン等の確認が必要です。', '',
        '## データ取得状況', '']
for source, status in DATA.get('status', {}).items():
    rows.append(f'- **{source}：** {safe(status)}')
rows.append('')
if DATA.get('warnings'):
    rows += ['## ⚠️ 取得時の注意', '']
    rows += ['- ' + safe(w) for w in DATA['warnings']]
    rows.append('')

for heading, group in [
    ('🎯 業務に関係しそうな情報', [x for x in DATA['items'] if any(t in x.get('search', '') for t in TERMS)]),
    ('🆕 その他の情報', [x for x in DATA['items'] if not any(t in x.get('search', '') for t in TERMS)])
]:
    rows += ['## ' + heading, '']
    if not group:
        rows += ['該当なし', '']
    for x in group[:40]:
        if x['source'] == 'CISA KEV':
            desc, ok1 = ja(x.get('description'))
            action, ok2 = ja(x.get('action'))
        else:
            desc, action, ok1, ok2 = x.get('description', ''), x.get('action', ''), True, True
        rows += [f"### {safe(x['title'])}", '',
                 f"**{safe(x['priority'])}** · {safe(x['source'])} · {safe(x['date'])}", '',
                 safe(desc or '概要なし'), '',
                 '**対策：** ' + safe(action or '公式情報を確認してください'), '']
        if not (ok1 and ok2):
            rows += ['> ⚠️ 自動翻訳に失敗したため、上記は英語原文です。', '']
        rows += [f"[公式情報を見る]({x['url']})", '', '---', '']

rows[7:7] = [f'> 翻訳状況：新規翻訳 {translated}件 / 翻訳失敗 {failed}件（過去の翻訳はキャッシュを再利用）', '']
(ROOT / 'REPORT.md').write_text('\n'.join(rows), encoding='utf-8')
CACHE_FILE.write_text(json.dumps(CACHE, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'翻訳: 新規{translated}件 / 失敗{failed}件')
