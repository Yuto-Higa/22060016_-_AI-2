import requests

def get_wikipedia_summary(query: str):
    """
    Wikipedia APIで指定語句の要約を取得する
    query: 検索キーワード（日本語/英語等）
    """
    url = "https://ja.wikipedia.org/api/rest_v1/page/summary/" + query
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    # 'extract'キーに要約テキストがある
    return {
        "title": data.get("title", ""),
        "description": data.get("description", ""),
        "extract": data.get("extract", ""),
        "thumbnail": data.get("thumbnail", {}).get("source", None),
        "content_urls": data.get("content_urls", {}).get("desktop", {}).get("page", None)
    }


