def recommend_places(city, interests, places):
    results = []

    for place in places:
        if place["city"] == city and place["category"] in interests:
            results.append(place)

    return results

def score_place(place, interests):
    score = 0

    # coincidencia con intereses
    if place["category"] in interests:
        score += 10

    # bonus por categoría “anime” (ejemplo de tu lógica)
    if place["category"] == "anime":
        score += 5

    # bonus base (lugares turísticos siempre suman algo)
    score += 2

    return score

def rank_places(places, interests):
    scored_places = []

    for place in places:
        score = score_place(place, interests)
        place_copy = place.copy()
        place_copy["score"] = score
        scored_places.append(place_copy)

    # ordenar de mayor a menor score
    scored_places.sort(key=lambda x: x["score"], reverse=True)

    return scored_places