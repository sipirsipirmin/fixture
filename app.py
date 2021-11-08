from flask import Flask
from datetime import datetime
import requests


HOURS_INTERVAL = {
    # script will check matches and past - feature range.(now is 0)
    "feature": 1,
    "past": -2
}

MATCH_EXIST = "1"
CRUCIAL_MATCH_EXIST = "2"
MATCH_NOT_EXIST = "0"

big_teams = [
    439, # BJK
    425, # FB
    2311, # GS
    4633 # TS
]

seconds_in_day = 24 * 60 * 60

app = Flask(__name__)

def get_matches():
    app.logger.info("getting matches from fixture service")
    matches = requests.get("https://apigateway.beinsports.com.tr/api/fixture/rewriteid/current/super-lig")
    match_data = matches.json()["Data"]

    return match_data


def get_delta_hours(match):
    match_date = match.get("matchDate")
    delta = datetime.now() - datetime.fromisoformat(match_date)
    delta_hours = (delta.days * seconds_in_day + delta.seconds)/360

    return delta_hours


@app.route("/check_matches")
def check_incoming_matches():
    matches = get_matches()
    now = datetime.now()
    for match in matches:
        delta_hours = get_delta_hours(match)
        if delta_hours < 1 and delta_hours > -2:
            if match.get("homeTeam") in big_teams or match.get("awayTeam") in big_teams:
                app.logger.info("crusial match found")
                return CRUCIAL_MATCH_EXIST
            return MATCH_EXIST
    return MATCH_NOT_EXIST
