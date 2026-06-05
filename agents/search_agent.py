
from ddgs import DDGS


class SearchAgent:
    def __init__(self):
        self.ddgs = DDGS()

    def search(self, query: str):
        """
        Searches web using DuckDuckGo and returns structured results.
        """

        try:
            search_results = self.ddgs.text(query, max_results=5)

            results = []

            if not search_results:
                return [{"title": "No results found", "link": "", "snippet": ""}]

            for result in search_results:
                results.append({
                    "title": result.get("title", ""),
                    "link": result.get("href", ""),
                    "snippet": result.get("body", "")
                })

            return results

        except Exception as e:
            return [{
                "title": "Search Error",
                "link": "",
                "snippet": str(e)
            }]
