
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()


class PlannerAgent:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("❌ GROQ_API_KEY not found. Check your .env file")

        self.client = Groq(api_key=api_key)

    def create_plan(self, user_query: str) -> str:
        """
        Converts user query into structured research steps.
        """

        prompt = f"""
You are an expert AI Research Planning Agent.

Break the user's request into clear, structured steps.

User Query:
{user_query}

Rules:
- Only return numbered steps
- Keep it concise and structured
- No explanations
"""

        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"Planner Error: {str(e)}"