import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load same model used for embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve(query, documents, top_k=5):
    # Convert query to embedding
    query_embedding = model.encode([query], convert_to_numpy=True)

    # Collect stored embeddings
    doc_embeddings = np.array([doc["embedding"] for doc in documents])

    # Compute cosine similarity
    similarities = cosine_similarity(query_embedding, doc_embeddings)[0]

    # Get top_k indices
    top_indices = similarities.argsort()[-top_k:][::-1]

    # Return top documents
    results = [documents[i] for i in top_indices]

    return results