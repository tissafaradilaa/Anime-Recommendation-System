import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("🚀 Loading recommender system...")

# =========================
# LOAD DATA (BATASI DEMO)
# =========================
anime = pd.read_csv("data/anime.csv").head(3000)
rating = pd.read_csv("data/rating.csv").head(100000)

anime['genre'] = anime['genre'].fillna('')
rating = rating[rating['rating'] != -1]

# =========================
# CONTENT-BASED SETUP
# =========================
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(anime['genre'])

anime_index = pd.Series(anime.index, index=anime['anime_id'])

# =========================
# USER–ITEM MATRIX
# =========================
user_item = rating.pivot_table(
    index='user_id',
    columns='anime_id',
    values='rating'
).fillna(0)

print("✅ Recommender system ready")

# =========================
# HYBRID ITEM-BASED
# =========================
def hybrid_recommendation(anime_name, alpha=0.6, top_n=10):
    row = anime[anime['name'].str.lower() == anime_name.lower()]
    if row.empty:
        return None

    anime_id = row.iloc[0]['anime_id']
    idx = anime_index[anime_id]

    # Content-based similarity (ON DEMAND)
    content_sim = cosine_similarity(
        tfidf_matrix[idx],
        tfidf_matrix
    ).flatten()

    cb_df = anime[['anime_id', 'name', 'genre']].copy()
    cb_df['content_score'] = content_sim

    if anime_id in user_item.columns:
        item_sim = cosine_similarity(
            user_item[anime_id].values.reshape(1, -1),
            user_item.T
        ).flatten()

        cf_df = pd.DataFrame({
            'anime_id': user_item.columns,
            'cf_score': item_sim
        })

        hybrid = cb_df.merge(cf_df, on='anime_id')
        hybrid['final_score'] = (
            alpha * hybrid['cf_score'] +
            (1 - alpha) * hybrid['content_score']
        )
    else:
        hybrid = cb_df.copy()
        hybrid['final_score'] = hybrid['content_score']

    return hybrid.sort_values('final_score', ascending=False).head(top_n)

# =========================
# USER-BASED HYBRID
# =========================
def hybrid_user_recommendation(user_id, alpha=0.6, top_n=10):
    if user_id not in user_item.index:
        return None

    user_sim = cosine_similarity(
        user_item.loc[[user_id]],
        user_item
    ).flatten()

    sim_users = pd.Series(user_sim, index=user_item.index)\
        .sort_values(ascending=False)[1:21]

    scores = {}
    watched = user_item.loc[user_id]
    watched = watched[watched > 0].index

    for other_user, sim in sim_users.items():
        ratings = user_item.loc[other_user]
        for anime_id, rating in ratings.items():
            if anime_id not in watched and rating > 0:
                scores[anime_id] = scores.get(anime_id, 0) + sim * rating

    if not scores:
        return None

    result = pd.DataFrame(scores.items(), columns=['anime_id', 'score'])
    result = result.merge(anime, on='anime_id')

    # user content profile
    genres = anime[anime['anime_id'].isin(watched)]['genre']
    profile = " ".join(genres)

    tfidf_user = tfidf.transform([profile])
    content_score = cosine_similarity(
        tfidf_user,
        tfidf_matrix
    ).flatten()

    result['content_score'] = result['anime_id'].map(
        dict(zip(anime['anime_id'], content_score))
    )

    result['final_score'] = (
        alpha * result['score'] +
        (1 - alpha) * result['content_score']
    )

    return result.sort_values('final_score', ascending=False).head(top_n)