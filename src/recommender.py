def recommend_places(city, interests, places):
    results = []

    for place in places:
        if place["city"] == city and place["category"] in interests:
            results.append(place)

    return results