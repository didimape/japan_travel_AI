# AI model class used to transform text into numerical vectors
# Pre-trained transformer model for semantic text embeddings
from sentence_transformers import SentenceTransformer, util

# all-MiniLM-L6-v2 -> Pre-trained NLP model that understands the meaning of sentences
# Load a pre-trained sentence transformer model for semantic similarity matching
model = SentenceTransformer('all-MiniLM-L6-v2')

# Intended to receive a dictionary of a place
# Convert place info into meaningful textual representation for 
# the AI model to work with it (for semantic embedding comparison)
def place_to_text(place):
    return f"{place['name']} {place['category']}"

def semantic_score(user_interests, place_text):
    # Concatenate into a single semantic query string
    user_text = " ".join(user_interests)

    # Text to numerical embedding vector
    # convert_to_tensor=True -> returns a PyTorch tensor instead of a Python list
    user_embedding = model.encode(user_text, convert_to_tensor=True)
    place_embedding = model.encode(place_text, convert_to_tensor=True)

    # Compute the semantic similarity score
    # It measures how close two vectors are (from 1 to -1, with 0 being unrelated)
    # Cosine similarity compares the angle between vectors
    # Smaller angle = more semantic similarity
    score = util.cos_sim(user_embedding, place_embedding)

    # score -> tensor object | .item() -> extracts the raw python float
    return score.item()

# Rank all places according to semantic relevance
def rank_places_ml(places, user_interests):
    results = []

    for place in places:
        text = place_to_text(place)
        # Calculates how relevant the place is to the user interests
        score = semantic_score(user_interests, text)

        # Avoid modifying the original data
        place_copy = place.copy()
        # Add a new field in the dictionary
        place_copy["score"] = score

        results.append(place_copy)

    # Sort places from highest score to lowest score
    results.sort(key=lambda x: x["score"], reverse=True)

    return results