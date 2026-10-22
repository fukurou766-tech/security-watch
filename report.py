
import json
import pathlib
import time

ROOT = pathlib.Path(__file__).resolve().parent
DATA = json.loads((ROOT / "data.json").read_text(encoding="utf-8"))

CACHE_FILE = ROOT / "translation_cache.json"
try:
    CACHE = json.loads(CACHE_FILE.read_text(encoding="utf-8")) if CACHE_FILE.exists() else {}
except (json.JSONDecodeError, OSError):
    CACHE = {}

TERMS = (
    "microsoft", "windows", "uipath", "chrome",
    "edge", "gitlab", "office", "sharepoint"
)

MAX_TRANSLATIONS = 12
REQUEST_INTERVAL = 4
MAX_TEXT_LENGTH = 4500

try:
    from deep_translator import GoogleTranslator
    translator = GoogleTranslator(source="en", target="ja")
except Exception as exc:
    translator = None
    print("翻訳機能の初期化失敗:", exc)

translated = 0
failed = 0
skipped = 0
rate_limited = False
last_request_time = None


def ja(text):
    global translated, failed, skipped, rate_limited, last_request_time

    text = str(text or "").strip()

    if not text:
        return "記載なし", True

    if text in CACHE:
        return CACHE[text], True

    if rate_limited or translated + failed >= MAX_TRANSLATIONS:
        skipped += 1
        return text, False

    if translator is None:
        failed += 1
        return text, False

    if len(text) > MAX_TEXT_LENGTH:
        skipped += 1
        return text, False

    try:
        # 翻訳成功・失敗に関係なくリクエスト間隔を空ける
        if last_request_time is not None:
            elapsed = time.monotonic() - last_request_time
            if elapsed < REQUEST_INTERVAL:
                time.sleep(REQUEST_INTERVAL - elapsed)

        last_request_time = time.monotonic()
        result = translator.translate(text)

        if not result:
            raise ValueError("翻訳結果が空です")

        CACHE[text] = result
        translated += 1
        return result, True

    except Exception as exc:
        failed += 1
        error_name = type(exc).__name__
        error_message = str(exc)

        print("翻訳失敗:", error_name, error_message[:250])

        if (
            "TooManyRequests" in error_name
            or "TooManyRequests" in error_message
            or "429" in error_message
        ):
            rate_limited = True
            print("アクセス制限を検出。今回の翻訳処理を停止します。")

        return text, False


def safe(text):
    return (
        str(text)
        .replace("\r", " ")
        .replace("\n", " ")
        .replace("<", "&lt;")
    )


rows = [
    "# 🛡️ 脆弱性情報ダッシュボード",
    "",
    f"**最終取得：{DATA['updated']}**",
    "",
    f"**取得件数：{len(DATA['items'])}件**（CISA直近35件・JVN最大40件）",
    "",
    "> ※CISA KEVは「悪用確認済み」の一覧です。掲載製品が自分の環境に影響するかは、バージョン等の確認が必要です。",
    "",
    "## データ取得状況",
    "",
]

for source, status in DATA.get("status", {}).items():
    rows.append(f"- **{source}：** {safe(status)}")

rows.append("")

if DATA.get("warnings"):
    rows += ["## ⚠️ 取得時の注意", ""]
    rows += ["- " + safe(w) for w in DATA["warnings"]]
    rows.append("")

for heading, group in [
    (
        "🎯 業務に関係しそうな情報",
        [
            x for x in DATA["items"]
            if any(t in x.get("search", "") for t in TERMS)
        ],
    ),
    (
        "🆕 その他の情報",
        [
            x for x in DATA["items"]
            if not any(t in x.get("search", "") for t in TERMS)
        ],
    ),
]:
    rows += ["## " + heading, ""]

    if not group:
        rows += ["該当なし", ""]

    for x in group[:40]:
        if x["source"] == "CISA KEV":
            desc, ok1 = ja(x.get("description"))
            action, ok2 = ja(x.get("action"))
        else:
            desc = x.get("description", "")
            action = x.get("action", "")
            ok1 = True
            ok2 = True

        rows += [
            f"### {safe(x['title'])}",
            "",
            f"**{safe(x['priority'])}** · {safe(x['source'])} · {safe(x['date'])}",
            "",
            safe(desc or "概要なし"),
            "",
            "**対策：** " + safe(action or "公式情報を確認してください"),
            "",
        ]

        if not (ok1 and ok2):
            rows += [
                "> ⚠️ 自動翻訳できなかったため、一部または全部が英語原文です。",
                "",
            ]

        rows += [
            f"[公式情報を見る]({x['url']})",
            "",
            "---",
            "",
        ]

# 翻訳状況をレポート上部に追加
status_message = (
    f"> 翻訳状況：新規翻訳 {translated}件 / "
    f"翻訳失敗 {failed}件 / "
    f"今回未翻訳 {skipped}件"
    "（過去の翻訳はキャッシュを再利用）"
)

if rate_limited:
    status_message += (
        "  \n> ⚠️ 翻訳サービスのアクセス制限を検出しました。"
        "次回実行時に再試行します。"
    )

rows[7:7] = [status_message, ""]

(ROOT / "REPORT.md").write_text(
    "\n".join(rows),
    encoding="utf-8"
)

CACHE_FILE.write_text(
    json.dumps(CACHE, ensure_ascii=False, indent=2),
    encoding="utf-8"
)

print(
    f"翻訳結果：成功 {translated}件 / "
    f"失敗 {failed}件 / 未翻訳 {skipped}件"
)