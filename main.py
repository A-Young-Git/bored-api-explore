import requests

BASE_URL = "https://bored-api.appbrewery.com"


def get_random_activity(BASE_URL: str) -> str:
    request = requests.get(f"{BASE_URL}/random")
    response = request.json()

    return response.get("activity")


activity = get_random_activity(BASE_URL)

print(
    f'3..2..1..You\'re randomly chosen activity is "{get_random_activity(BASE_URL)}."'
)
