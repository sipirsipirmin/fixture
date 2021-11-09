from datetime import datetime
from sys import maxsize
import requests
from flask import Flask
from settings import *


app = Flask(__name__)

def get_matches():
    app.logger.info("Getting matches from fixture service")
    matches = requests.get("https://apigateway.beinsports.com.tr/api/fixture/rewriteid/current/super-lig")
    match_data = matches.json()["Data"]

    return match_data


def get_delta_hours(match):
    match_date = match.get("matchDate")
    if match_date == None:
        return maxsize
    try:
        delta = datetime.now() - datetime.fromisoformat(match_date)
        delta_hours = (delta.days * SECONDS_IN_DAY + delta.seconds)/360
    except Exception as e:
        app.logger.exception("An error occured when caculating estimated time to match match id=%s " %match.get("id"))
        delta_hours = maxsize

    return delta_hours


@app.route("/check_matches")
def check_incoming_matches():
    matches = get_matches()
    
    for match in matches:
        delta_hours = get_delta_hours(match)
        if delta_hours < HOURS_INTERVAL["feature"] or delta_hours > HOURS_INTERVAL["past"]*-1:
            if match.get("homeTeam") in BIG_TEAMS or match.get("awayTeam") in BIG_TEAMS:
                app.logger.info("Crusial match found!")
                return CRUCIAL_MATCH_EXIST
            return MATCH_EXIST
    return MATCH_NOT_EXIST
