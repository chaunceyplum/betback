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
  return("Hello world")

@app.get("/get_all_active_players")
def get_active_players(): 
    return get_players()

@app.get("/get_player_info")
def get_player_info():
    player_info =  playergamelog.PlayerGameLog(player_id='203999',season='2023-2024',season_type_all_star='Regular Season')
    return player_info.get_dict()

@app.get("/get_player/{player_id}")
def get_player(player_id):
    player_info = playercareerstats.PlayerCareerStats(player_id=player_id)
    return player_info.get_dict()
