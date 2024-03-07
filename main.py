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
    career = playercareerstats.PlayerCareerStats(player_id='203999') 

    return career.get_dict()
 # return("Hello world")

@app.get("/get_all_active_players")
def get_active_players():
    # active_players = get_active_players()
    return get_players()



# @app.get("/get_player_info")
# def get_player_info():
#     player_info =playerindex()
#     return

@app.get("/get_player_info")
async def get_player_game_log_info():
    player_info = await playergamelog.PlayerGameLog(player_id='203999',season='2023-2024',season_type_all_star='Regular Season')
    return player_info.get_dict()

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# Nikola Jokić
# career = playercareerstats.PlayerCareerStats(player_id='203999') 

# # pandas data frames (optional: pip install pandas)
# # career.get_data_frames()[0]

# # json
# career.get_json()

# # dictionary
# print(career.get_dict())