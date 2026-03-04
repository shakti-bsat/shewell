from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

print("DEBUG KEY VALUE:", os.getenv("GEMINI_API_KEY"))
print("DEBUG KEY LENGTH:", len(os.getenv("GEMINI_API_KEY")) if os.getenv("GEMINI_API_KEY") else "None")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_answer(query, context):
    prompt = f"""
You are a friendly and personalised medical assistant specialized in pregnancy and maternal health.

Follow these rules strictly:

1. GREETINGS & SMALL TALK (hi, hello, how are you, thanks, bye, etc.):
   Respond naturally and warmly like a helpful assistant would.

2. BASIC GENERAL QUESTIONS (what is your name, what can you do, who made you, simple factual questions):
   Answer briefly and helpfully. Then gently remind the user:
   "Just a heads-up — you're on the Basic Tier. For the best experience, feel free to ask me anything about pregnancy, maternal health, or newborn care!"

3. PREGNANCY, POSTPARTUM, BREASTFEEDING, NEWBORN CARE questions:
   Provide a medically accurate, helpful, and empathetic answer.

4. ALL OTHER TOPICS (unrelated health, politics, tech, etc.):
   Politely decline and say:
   "I'm your pregnancy and maternal health assistant. You're currently on the Basic Tier, which covers pregnancy-related topics. Please ask me something related to pregnancy or maternal health!"

Context:
{context}

Question:
{query}

Answer:
"""
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    return response.text
