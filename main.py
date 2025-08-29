import requests
import polars as pl

BASE_URL = "https://bored-api.appbrewery.com"


def get_random_activity(base_url: str) -> str:
    response = requests.get(f"{base_url}/random").json()

    return response.get("activity")


def get_kid_friendly_activities(
    base_url: str, activity_type: str, participants: int
) -> int:
    response = requests.get(
        f"{base_url}/filter?type={activity_type}&participants={participants}"
    ).json()

    # Convert to Polars dataframe
    data = pl.DataFrame(response)
    return data.filter(pl.col("kidFriendly")).shape[0]


random_activity = get_random_activity(BASE_URL)
print(f'3..2..1..You\'re randomly chosen activity is "{random_activity}."\n')


kid_friendly_activities_count = get_kid_friendly_activities(
    BASE_URL, activity_type="education", participants=1
)
print(
    f"There are {kid_friendly_activities_count} kid friendly activities in this dataset."
)
