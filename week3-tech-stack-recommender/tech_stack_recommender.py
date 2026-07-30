"""
Project 3: AI Recommendation Logic - Tech Stack Recommender
DecodeLabs - AI Internship (Batch 2026)

Goal: Map a user's raw skills to the most relevant job roles using
Content-Based Filtering (TF-IDF + Cosine Similarity).

Pipeline (IPO Model):
  INPUT   -> User provides 3+ skills
  PROCESS -> TF-IDF vectorization + Cosine Similarity scoring
  OUTPUT  -> Top-3 ranked job role recommendations
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ---------------------------------------------------------
# STEP 1: INGESTION - Load the job role dataset
# ---------------------------------------------------------
df = pd.read_csv("raw_skills.csv")

print("=" * 55)
print("STEP 1: DATASET LOADED")
print("=" * 55)
print(f"Total job roles in database: {len(df)}")
print(df[["job_role"]].to_string(index=False))


def get_recommendations(user_skills, dataframe, top_n=3):
    """
    Takes a list of user skills and returns the top_n best-matching
    job roles using TF-IDF weighting + Cosine Similarity.
    """
    # Combine the user's skills into one "document" for vectorization
    user_profile_text = " ".join(user_skills)

    # All job-role skill sets + the user profile, so they share
    # the exact same vocabulary space (required for TF-IDF to work)
    corpus = dataframe["skills"].tolist() + [user_profile_text]

    # ---------------------------------------------------------
    # STEP 2: SCORING - Vectorize with TF-IDF, then Cosine Similarity
    # ---------------------------------------------------------
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Last row of the matrix is the user's vector
    user_vector = tfidf_matrix[-1]
    job_vectors = tfidf_matrix[:-1]

    similarity_scores = cosine_similarity(user_vector, job_vectors).flatten()

    # ---------------------------------------------------------
    # STEP 3: SORTING - Rank job roles by similarity score
    # ---------------------------------------------------------
    results = dataframe.copy()
    results["match_score"] = similarity_scores
    results = results.sort_values(by="match_score", ascending=False)

    # ---------------------------------------------------------
    # STEP 4: FILTERING - Return only the Top-N matches
    # ---------------------------------------------------------
    return results.head(top_n)[["job_role", "match_score"]]


# ---------------------------------------------------------
# STEP 1 (continued): Take user input (minimum 3 skills)
# ---------------------------------------------------------
def get_user_skills():
    print("\n" + "=" * 55)
    print("STEP 2: ENTER YOUR SKILLS")
    print("=" * 55)
    print("Enter at least 3 skills, one at a time.")
    print("Type 'done' when finished (after at least 3 entries).\n")

    skills = []
    while True:
        skill = input(f"Skill #{len(skills) + 1}: ").strip()
        if skill.lower() == "done":
            if len(skills) >= 3:
                break
            else:
                print("Please enter at least 3 skills before typing 'done'.")
                continue
        if skill:
            skills.append(skill)
    return skills


if __name__ == "__main__":
    user_skills = get_user_skills()

    print("\n" + "=" * 55)
    print("STEP 3: MATCHING PREFERENCES")
    print("=" * 55)
    print(f"Your skills: {user_skills}")

    top_matches = get_recommendations(user_skills, df, top_n=3)

    print("\n" + "=" * 55)
    print("STEP 4: TOP 3 RECOMMENDED CAREER PATHS")
    print("=" * 55)
    for rank, (_, row) in enumerate(top_matches.iterrows(), start=1):
        print(f"{rank}. {row['job_role']}  (Match Score: {row['match_score']:.2%})")
