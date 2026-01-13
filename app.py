from flask import Flask, render_template, request
from recommender import (
    hybrid_recommendation,
    hybrid_user_recommendation,
    anime
)

app = Flask(__name__)

anime_list = sorted(anime['name'].dropna().unique())
anime_map = {name.lower(): name for name in anime_list}

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = None
    selected_anime = None
    error = None

    if request.method == "POST":
        selected_anime = request.form["anime"]
        key = selected_anime.lower()

        if key not in anime_map:
            error = "Anime tidak ditemukan. Silakan pilih dari daftar."
        else:
            recommendations = hybrid_recommendation(anime_map[key])

    return render_template(
        "index.html",
        anime_list=anime_list,
        recommendations=recommendations,
        selected_anime=selected_anime,
        error=error
    )

@app.route("/user", methods=["GET", "POST"])
def user_mode():
    recommendations = None
    error = None
    user_id = None

    if request.method == "POST":
        try:
            user_id = int(request.form["user_id"])
            recommendations = hybrid_user_recommendation(user_id)

            if recommendations is None:
                error = "User ID tidak ditemukan atau data tidak cukup."

        except ValueError:
            error = "User ID harus berupa angka."

    return render_template(
        "user.html",
        recommendations=recommendations,
        error=error,
        user_id=user_id if recommendations is not None else None
    )

if __name__ == "__main__":
    app.run(debug=True)