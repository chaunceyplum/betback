from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playerindex
from nba_api.stats.endpoints import playergamelog

from nba_api.stats.static.players import get_active_players
from nba_api.stats.static.players import get_players

from typing import Union
import json
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    # career = playercareerstats.PlayerCareerStats(player_id='203999') 

    # return career.get_dict()
  return("Hello world")

@app.get("/get_all_active_players")
def get_active_players():
    # active_players = get_active_players()
    return get_players()


#blah
# @app.get("/get_player_info")
# def get_player_info():
#     player_info =playerindex()
#     return

@app.get("/get_player_info")
async def get_player_game_log_info():
    player_info = await playergamelog.PlayerGameLog(player_id='203999',season='2023-2024',season_type_all_star='Regular Season')
    return player_info.get_dict()

@app.get("/get_player/{player_id}")
async def read_item(player_id):
    player_info = await playergamelog.PlayerCarrerStats(player_id=player_id)
    return player_info.get_dict()

# Nikola Jokić
# career = playercareerstats.PlayerCareerStats(player_id='203999') 

# # pandas data frames (optional: pip install pandas)
# # career.get_data_frames()[0]

# # json
# career.get_json()

# # dictionary
# print(career.get_dict())