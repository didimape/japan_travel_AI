from data.places import places
from src.embeddings import rank_places_ml
from src.planner import build_itinerary

user = {
    "city": "Tokyo",
    "days": 2,
    "interests": ["I like arcades and anime", "I want to see temples", "I enjoy nature and parks"]
}

ranked = rank_places_ml(places, user["interests"])

print("🏆 RANKING DE LUGARES:\n")
for r in ranked:
    print(f"{r['name']} - score: {r['score']}")

itinerary = build_itinerary(ranked, user["days"])

print("\n🧭 ITINERARIO:\n")

for i, day in enumerate(itinerary):
    print(f"Día {i+1}:")
    for place in day:
        print(f" - {place['name']} ({place['category']})")
    print()