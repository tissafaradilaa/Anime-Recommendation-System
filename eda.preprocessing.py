import pandas as pd

anime = pd.read_csv("data/anime.csv")
rating = pd.read_csv("data/rating.csv")

print("Sebelum preprocessing:")
print("Total anime:", anime.shape[0])
print("Genre kosong:", anime['genre'].isna().sum())
print("Total rating:", rating.shape[0])
print("Rating -1:", (rating['rating'] == -1).sum())

# preprocessing
anime['genre'] = anime['genre'].fillna('')
rating = rating[rating['rating'] != -1]

print("\nSesudah preprocessing:")
print("Total anime:", anime.shape[0])
print("Genre kosong:", anime['genre'].isna().sum())
print("Total rating:", rating.shape[0])