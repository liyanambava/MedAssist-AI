import requests

HEADERS = {
    "User-Agent": "MedAssistAI/1.0 (educational project)"
}

def get_nearby_clinics(city, limit=5):
    """
    Reliable healthcare facility lookup using Nominatim text search.
    Works well for Indian cities.
    """

    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": f"hospitals in {city}",
        "format": "jsonv2",
        "limit": limit,
        "addressdetails": 1
    }

    response = requests.get(url, params=params, headers=HEADERS, timeout=30)

    if response.status_code != 200:
        return []

    data = response.json()
    clinics = []

    for place in data:
        clinics.append({
            "name": place.get("display_name", "Healthcare Facility"),
            "lat": place.get("lat"),
            "lon": place.get("lon")
        })

    return clinics
