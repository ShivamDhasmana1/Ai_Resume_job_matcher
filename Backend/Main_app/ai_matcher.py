from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def ai_match_jobs(resume_text, jobs):
    """
    Uses TF-IDF + Cosine Similarity to find best job matches for the resume text.
    """
    # Combine all job descriptions into a list
    job_texts = [job["description"] for job in jobs]
    
    # Add the resume text to the end of the list for comparison
    corpus = job_texts + [resume_text]
    
    # Convert text data to numerical vectors
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    # Calculate cosine similarity between resume and all job descriptions
    similarity_scores = cosine_similarity(tfidf_matrix[-1:], tfidf_matrix[:-1]).flatten()
    
    # Sort jobs by similarity (descending)
    ranked_indices = similarity_scores.argsort()[::-1]
    
    # Prepare top results
    top_matches = []
    for idx in ranked_indices[:5]:  # top 5 matches
        top_matches.append({
            "job_title": jobs[idx]["title"],
            "company": jobs[idx]["company"],
            "match_score": round(similarity_scores[idx] * 100, 2)
        })
    
    return top_matches
