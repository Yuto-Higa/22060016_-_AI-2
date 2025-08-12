import streamlit as st
from logic import get_wikipedia_summary
import pandas as pd
from datetime import datetime
import os

HISTORY_FILE = r"C:\AIprogramming\streamlit\kadai2\log\search_history.csv"

def save_search_to_csv(keyword, result):
    if result is None:
        return

    data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "keyword": keyword,
        "title": result["title"],
        "url": result["content_urls"]
    }

    df = pd.DataFrame([data])

    if os.path.exists(HISTORY_FILE):
        df.to_csv(HISTORY_FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(HISTORY_FILE, mode='w', header=True, index=False)

st.title("📚 Wikipedia要約検索アプリ")

query = st.text_input("検索キーワードを入力してください（例: 富士山）")

if st.button("検索"):
    if not query.strip():
        st.warning("キーワードを入力してください。")
    else:
        result = get_wikipedia_summary(query.strip())
        if result:
            save_search_to_csv(query.strip(), result)
            st.subheader(result["title"])
            if result["thumbnail"]:
                st.image(result["thumbnail"], width=200)
            if result["description"]:
                st.caption(result["description"])
            st.write(result["extract"])
            if result["content_urls"]:
                st.markdown(f"[Wikipedia記事全文はこちら]({result['content_urls']})")
        else:
            st.error("該当する記事が見つかりませんでした。")

# 検索履歴を表示
st.markdown("---")
if st.checkbox("🔍 検索履歴を表示"):
    if os.path.exists(HISTORY_FILE):
        history_df = pd.read_csv(HISTORY_FILE)
        st.dataframe(history_df)
    else:
        st.info("検索履歴はまだありません。")

