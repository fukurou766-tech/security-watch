
import json
import os
import pathlib
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
DATA = json.loads((ROOT / "data.json").read_text(encoding="utf-8"))
CACHE_FILE = ROOT / "translation_cache.json"
try:
    CACHE = json.loads(CACHE_FILE.read_text(encoding="utf-8")) if CACHE_FILE.exists() else {}
except (OSError, json.JSONDecodeError):
    CACHE = {}

TERMS = ("microsoft", "windows", "uipath", "chrome", "edge", "gitlab", "office", "sharepoint")
API_KEY = os.environ.get("DEEPL_API_KEY", "").strip()
API_URL = os.environ.get("DEEPL_API_URL", "https://api-free.deepl.com/v2/translate")
MAX_NEW_TRANSLATIONS = 40
translated = 0
failed = 0
skipped = 0

def ja(value):
    global translated, failed, skipped
    text = str(value or "").strip()
    if not text:
        return "記載なし", True
    key = "deepl-ja:" + text
    if key in CACHE:
        return CACHE[key], True
    if translated + failed >= MAX_NEW_TRANSLATIONS:
        skipped += 1
        return text, False
    if not API_KEY:
        failed += 1
        print("翻訳失敗: DEEPL_API_KEY が設定されていません")
        return text, False
    try:
        payload = json.dumps({"text": [text], "source_lang": "EN", "target_lang": "JA"}).encode("utf-8")
        request = urllib.request.Request(
            API_URL, data=payload,
            headers={"Authorization": "DeepL-Auth-Key " + API_KEY, "Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.load(response)["translations"][0]["text"].strip()
        if not result:
            raise ValueError("翻訳結果が空です")
        CACHE[key] = result
        translated += 1
        return result, True
    except urllib.error.HTTPError as exc:
        failed += 1
        print(f"DeepL翻訳失敗: HTTP {exc.code}")
        return text, False
    except Exception as exc:
        failed += 1
        print("DeepL翻訳失敗:", type(exc).__name__, str(exc)[:180])
        return text, False

def safe(value):
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace("\r", " ").replace("\n", " ")

rows = [
    "# 🛡️ 脆弱性情報ダッシュボード", "",
    f"**最終取得：{safe(DATA['updated'])}**", "",
    f"**取得件数：{len(DATA['items'])}件**（CISA直近35件・JVN最大40件）", "",
    "> ※CISA KEVは「悪用確認済み」の一覧です。掲載製品が自分の環境に影響するかは、バージョン等の確認が必要です。", "",
    "## データ取得状況", ""
]
for source, status in DATA.get("status", {}).items():
    rows.append(f"- **{safe(source)}：** {safe(status)}")
rows.append("")
if DATA.get("warnings"):
    rows += ["## ⚠️ 取得時の注意", ""]
    rows += ["- " + safe(w) for w in DATA["warnings"]]
    rows.append("")

for heading, group in [
    ("🎯 業務に関係しそうな情報", [x for x in DATA["items"] if any(t in x.get("search", "") for t in TERMS)]),
    ("🆕 その他の情報", [x for x in DATA["items"] if not any(t in x.get("search", "") for t in TERMS)])
]:
    rows += ["## " + heading, ""]
    if not group:
        rows += ["該当なし", ""]
    for x in group[:40]:
        if x["source"] == "CISA KEV":
            desc, ok1 = ja(x.get("description"))
            action, ok2 = ja(x.get("action"))
        else:
            desc, action, ok1, ok2 = x.get("description", ""), x.get("action", ""), True, True
        rows += [
            f"### {safe(x['title'])}", "",
            f"**{safe(x['priority'])}** · {safe(x['source'])} · {safe(x['date'])}", "",
            safe(desc or "概要なし"), "",
            "**対策：** " + safe(action or "公式情報を確認してください"), ""
        ]
        if not (ok1 and ok2):
            rows += ["> ⚠️ 自動翻訳できなかったため、一部または全部が英語原文です。", ""]
        rows += [f"[公式情報を見る]({x['url']})", "", "---", ""]

rows[7:7] = [
    f"> DeepL翻訳状況：新規翻訳 {translated}件 / 翻訳失敗 {failed}件 / 今回未翻訳 {skipped}件（キャッシュ再利用あり）", ""
]
(ROOT / "REPORT.md").write_text("\n".join(rows), encoding="utf-8")
CACHE_FILE.write_text(json.dumps(CACHE, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"DeepL翻訳：成功 {translated}件 / 失敗 {failed}件 / 未翻訳 {skipped}件")