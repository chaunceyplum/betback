from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playerindex
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static.players import get_active_players
from nba_api.stats.static.players import get_players
from nba_api.stats.static import players
from typing import Union
import json
import requests
from fastapi import FastAPI
from datetime import datetime, timedelta
import json
app = FastAPI()


@app.get("/")
def read_root():
  return("Hello world")

@app.get("/get_all_active_players")
async def get_all_active_players():
    allPlayers = []
    # r = requests.get('https://nba-stats-db.herokuapp.com/api/playerdata/season/2023/').json
    total_pages= 8
    # print(r)
    for page in range(1, total_pages):

        url = "https://nba-stats-db.herokuapp.com/api/playerdata/season/2023/?page="+str(page)              
        response = requests.get(url=url ).json()
        # print(response["results"])   
        pagey = response["results"]
        for record in pagey:
            allPlayers.append(record)
        # allPlayers.append(response["results"])       
        page += 1

    # prettify JSON
    # data = json.dumps(allPlayers, sort_keys=True, indent=4)

    return {"data": str(allPlayers)}

# @app.get("/get_player_info")
# def get_player_info():
#     player_info =  playergamelog.PlayerGameLog(player_id='203999',season='2023-2024',season_type_all_star='Regular Season')
#     return player_info.get_dict()

@app.get("/get_player/{player_id}")
def get_player(player_id:int):
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)

    data = {"data":player_info}
    return data.get_dict()
    # player = players.find_player_by_id(player_id=player_id)
    # today = datetime.now()
    # today += timedelta(days=5)
    # iso_date = today.isoformat()
    # player_info =  playergamelog.PlayerGameLog(player_id=player_id,season='2023-2024',season_type_all_star='Regular Season', date_from_nullable=iso_date)
    # return player_info.get_dict()
    # return player
