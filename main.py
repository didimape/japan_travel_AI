from data.places import places
from src.recommender import recommend_places

user = {
    "city": "Tokyo",
    "days": 2,
    "interests": ["anime", "food"]
}

recs = recommend_places(
    user["city"],
    user["interests"],
    places
)

print("Recomendaciones:\n")

for r in recs:
    print(f"- {r['name']} ({r['category']})")