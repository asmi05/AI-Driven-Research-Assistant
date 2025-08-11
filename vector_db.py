import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def build_vector_db(papers):
    embeddings = model.encode([p['summary'] for p in papers])
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, embeddings, papers

def suggest_related(query, index, embeddings, papers, top_k=3):
    query_emb = model.encode([query])
    distances, indices = index.search(np.array(query_emb), top_k)
    return [papers[i] for i in indices[0]]

# Example: After searching, build db and suggest.