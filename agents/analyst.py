
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()


class AnalystAgent:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("❌ GROQ_API_KEY not found. Check .env file")

        self.client = Groq(api_key=api_key)

    def analyze(self, research_data):
        if not research_data:
            return "No research data provided for analysis."

        prompt = f"""
You are a senior business strategy analyst.

Analyze the following research findings deeply.

Provide:

1. Market Opportunities
2. Major Challenges
3. Competitive Advantages
4. Business Risks
5. Strategic Recommendations

Research Data:
{research_data}
"""

        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"Analyst Error: {str(e)}"