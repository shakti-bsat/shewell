import requests

def generate_answer(query, context):
    prompt = f"""
You are a medical assistant specialized ONLY in pregnancy and maternal health.

If the question is about pregnancy, postpartum care, breastfeeding, or newborn care:
Provide a medically accurate general answer.

If the question is outside pregnancy or maternal health:
Politely refuse.

Context:
{context}

Question:
{query}

Answer:
"""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gpt-oss",
            "prompt": prompt,
            "stream": False
        }
    )

    # print(response.json())
    # return response.json()

    return response.json()["response"]