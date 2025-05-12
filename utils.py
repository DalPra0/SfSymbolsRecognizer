from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')  # Small and fast

def encode_descriptions(symbols):
    descriptions = [s["description"] for s in symbols]
    return model.encode(descriptions, convert_to_tensor=True)

def semantic_search(query, symbols, symbol_embeddings, top_k=5):
    query_embedding = model.encode([query], convert_to_tensor=True)
    similarities = cosine_similarity(query_embedding, symbol_embeddings)[0]
    top_indices = similarities.argsort()[::-1][:top_k]
    return [symbols[i] for i in top_indices]
