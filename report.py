import json,pathlib,datetime,re
p=pathlib.Path(__file__).parent
d=json.loads((p/'data.json').read_text(encoding='utf-8'))
terms=['microsoft','windows','uipath','chrome','edge','gitlab','office','sharepoint']
def esc(s):return str(s).replace('|','\\|').replace('\n',' ')
rows=['# 🛡️ 脆弱性情報ダッシュボード','',f"**最終取得：{d['updated']}**",'',f"**取得件数：{len(d['items'])}件**（CISA KEVの直近35件とJVNの直近40件を上限）",'','> ⚠️ CISAの英語本文は翻訳APIを使用していないため、英語原文です。Android Chromeの「翻訳」で日本語表示できます。','']
if d['errors']:rows+=['## 取得時の注意']+['- '+x for x in d['errors']]+['']
for heading,arr in [('🎯 業務に関係しそうな情報',[x for x in d['items'] if any(t in x['search'] for t in terms)]),('🆕 その他の新着情報',[x for x in d['items'] if not any(t in x['search'] for t in terms)])]:
 rows+=['## '+heading,'']
 if not arr:rows+=['該当なし','']
 for x in arr[:40]:
  rows+=['### '+x['title'],f"**{x['priority']}** · {x['source']} · {x['date']}", '',x['description'] or '概要なし','',f"**対策：** {x['action']}",'',f"[公式情報を見る]({x['url']})",'','---','']
(p/'REPORT.md').write_text('\n'.join(rows),encoding='utf-8')
