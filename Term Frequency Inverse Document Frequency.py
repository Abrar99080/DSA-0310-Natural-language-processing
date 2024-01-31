from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
documents = [
    "The quick brown fox jumps over the lazy dog",
    "A brown dog jumped over a fox",
    "The dog is quick and brown",
    "The cat is black",
    "A black cat and a brown dog are friends",
]
query = "quick brown fox"
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
query_tfidf = tfidf_vectorizer.transform([query])
cosine_similarities = linear_kernel(query_tfidf, tfidf_matrix)
document_scores = list(enumerate(cosine_similarities[0]))
document_scores.sort(key=lambda x: x[1], reverse=True)
top_n = 3
top_documents = document_scores[:top_n]
for i, score in top_documents:
    print(f"Document {i + 1}: {documents[i]} (Score: {score:.2f})")
