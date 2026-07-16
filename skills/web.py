from duckduckgo_search import DDGS

def search_web(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))

        if not results:
            return None

        answer = "Here's what I found:\n\n"

        for result in results:
            answer += f"• {result['title']}\n"
            answer += f"{result['body']}\n\n"

        return answer

    except Exception:
        return None