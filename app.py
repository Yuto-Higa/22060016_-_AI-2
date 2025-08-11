import streamlit as st
from logic import get_wikipedia_summary

st.title("📚 Wikipedia要約検索アプリ")

query = st.text_input("検索キーワードを入力してください（例: 富士山）")

if st.button("検索"):
    if not query.strip():
        st.warning("キーワードを入力してください。")
    else:
        result = get_wikipedia_summary(query.strip())
        if result:
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
