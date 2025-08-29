import requests
import polars as pl

BASE_URL = "https://bored-api.appbrewery.com"


def get_random_activity(BASE_URL: str) -> str:
    request = requests.get(f"{BASE_URL}/random")
    response = request.json()

    return response.get("activity")


def get_kid_friendly_activities(
    BASE_URL: str, activity_type: str, participants: int
) -> int:
    request = requests.get(
        f"{BASE_URL}/filter?type={activity_type}&participants={participants}"
    )
    response = request.json()

    # Convert to Polars dataframe
    data = pl.DataFrame(response)
    kid_friendly_activities = data.get_column("kidFriendly").count()

    return kid_friendly_activities


# random_activity = get_random_activity(BASE_URL)
# print(f'3..2..1..You\'re randomly chosen activity is "{random_activity}."')


kid_friendly_activities = get_kid_friendly_activities(
    BASE_URL, activity_type="education", participants=1
)
print(f"There are {kid_friendly_activities} kid friendly activities in this dataset.")
