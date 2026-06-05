
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()


class ResearchAgent:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("❌ GROQ_API_KEY not found. Check .env file")

        self.client = Groq(api_key=api_key)

    def analyze_search_results(self, query, search_results):
        combined_text = ""

        # Safe handling of search results
        if not search_results:
            search_results = []

        for result in search_results:
            combined_text += f"""
Title: {result.get("title", "")}
Snippet: {result.get("snippet", "")}

"""

        prompt = f"""
You are an expert Research Analysis Agent.

Your job is to analyze search findings
and extract useful insights.

Original Query:
{query}

Search Results:
{combined_text}

Instructions:
- Summarize key findings
- Remove noise
- Focus on insights
- Keep professional output
"""

        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"Research Error: {str(e)}"