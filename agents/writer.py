
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()


class WriterAgent:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("❌ GROQ_API_KEY not found. Check .env file")

        self.client = Groq(api_key=api_key)

    def write_report(self, analysis):
        if not analysis:
            return "No analysis data provided for report generation."

        prompt = f"""
You are a professional business report writer.

Convert the following analysis into a structured professional report.

Include:

1. Executive Summary
2. Market Overview
3. Opportunities
4. Challenges
5. Strategic Recommendations
6. Future Scope
7. Conclusion

Analysis:
{analysis}
"""

        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"Writer Error: {str(e)}"