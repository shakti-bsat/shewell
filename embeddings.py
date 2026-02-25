from sentence_transformers import SentenceTransformer

# Load model once (global load = efficient)
model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(documents):
    texts = [doc["text"] for doc in documents]

    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        convert_to_numpy=True
    )

    # Attach embeddings back to documents
    for doc, embedding in zip(documents, embeddings):
        doc["embedding"] = embedding.tolist()

    return documents