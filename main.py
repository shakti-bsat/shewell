from cleanner import clean_text
from chunky import chunk
from embeddings import generate_embeddings
from retriever import retrieve
from generator import generate_answer

import json

def is_pregnancy_related(query):
    keywords = [
        "pregnancy", "pregnant", "postpartum", "post pregnancy",
        "breastfeeding", "delivery", "labor", "trimester",
        "fetus", "prenatal", "maternal", "miscarriage",
        "c-section", "newborn", "baby"
    ]

    query_lower = query.lower()
    return any(word in query_lower for word in keywords)

if __name__ == "__main__":

    with open("site_scraper/data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    filtered_data = []

    for item in data:
        url = item["url"].lower()

        if any(x in url for x in ["privacy", "terms", "login", "register", "auth"]):
            continue

        content = item["content"]

        if "Quick Links" in content:
            content = content.split("Quick Links")[0]

        cleaned = clean_text(content)

        filtered_data.append({
            "url": item["url"],
            "title": item.get("title", ""),
            "content": cleaned
        })
    documents = chunk(filtered_data)

    documents_with_embeddings = generate_embeddings(documents)


    while True:
        query = input("\nAsk a question (or type exit): ")

        if query.lower() == "exit":
            break

        if not is_pregnancy_related(query):
            print("I am a pregnancy-focused assistant. Please ask questions related to pregnancy or maternal health.")
            continue

        results = retrieve(query, documents_with_embeddings, top_k=3)

        context = "\n\n".join([doc["text"] for doc in results])

        answer = generate_answer(query, context)

        print(answer)