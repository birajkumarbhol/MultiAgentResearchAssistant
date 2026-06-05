from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()


class ReviewerAgent:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("❌ GROQ_API_KEY not found")

        self.client = Groq(api_key=api_key)

    def review(self, report):
        if not report:
            return "No report provided for review."

        prompt = f"""
You are a senior quality assurance analyst.

Review the following business report and improve it.

Your tasks:
- Improve clarity
- Fix grammar issues
- Remove repetition
- Ensure professional tone
- Enhance structure
- Do NOT change meaning

Report:
{report}
"""

        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"Reviewer Error: {str(e)}"