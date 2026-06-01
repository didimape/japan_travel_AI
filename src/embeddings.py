from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def place_to_text(place):
    return f"{place['name']} {place['category']}"

def semantic_score(user_interests, place_text):
    user_text = " ".join(user_interests)

    user_embedding = model.encode(user_text, convert_to_tensor=True)
    place_embedding = model.encode(place_text, convert_to_tensor=True)

    score = util.cos_sim(user_embedding, place_embedding)

    return score.item()

def rank_places_ml(places, user_interests):
    results = []

    for place in places:
        text = place_to_text(place)
        score = semantic_score(user_interests, text)

        place_copy = place.copy()
        place_copy["score"] = score

        results.append(place_copy)

    results.sort(key=lambda x: x["score"], reverse=True)

    return results