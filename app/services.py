import requests
from .schemas import PlayerResponse

API_URL = "https://cors-proxy-90954623675.europe-west1.run.app/"


def get_magnificent_7():
    data = fetch_data()
    players = data["elements"]
    return select_magnificent_7(players)


def get_team_magnificent_7(team_id: int):
    data = fetch_data()
    players = data["elements"]
    team_players = [p for p in players if p["team"] == team_id]
    return select_magnificent_7(team_players)


def fetch_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch data from API")


def select_magnificent_7(players):
    players = calculate_magnificence(players)

    goalkeepers = [p for p in players if p["element_type"] == 1]
    defenders = [p for p in players if p["element_type"] == 2]
    midfielders = [p for p in players if p["element_type"] == 3]
    forwards = [p for p in players if p["element_type"] == 4]

    goalkeepers.sort(key=lambda p: p["magnificence"], reverse=True)
    defenders.sort(key=lambda p: p["magnificence"], reverse=True)
    midfielders.sort(key=lambda p: p["magnificence"], reverse=True)
    forwards.sort(key=lambda p: p["magnificence"], reverse=True)

    def format_player(player):
        return PlayerResponse(
            first_name=player["first_name"],
            last_name=player["second_name"],
            web_name=player["web_name"],
            goals_scored=player["goals_scored"],
            assists=player["assists"],
        )

    magnificent_7 = {
        "goalkeeper": format_player(goalkeepers[0]) if goalkeepers else None,
        "defenders": [format_player(p) for p in defenders[:2]],
        "midfielders": [format_player(p) for p in midfielders[:3]],
        "forward": format_player(forwards[0]) if forwards else None,
    }

    return magnificent_7


def calculate_magnificence(players):
    for player in players:
        player["magnificence"] = player.get("goals_scored", 0) + player.get(
            "assists", 0
        )
    return players
