def build_itinerary(places, days, max_hours_per_day=6):
    itinerary = [[] for _ in range(days)]
    day_hours = [0] * days

    current_day = 0

    for place in places:
        duration = place.get("duration", 2)

        # si no cabe en el día actual, pasamos al siguiente
        while (day_hours[current_day] + duration > max_hours_per_day):
            current_day += 1

            if current_day >= days:
                return itinerary  # ya no hay más días

        itinerary[current_day].append(place)
        day_hours[current_day] += duration

    return itinerary