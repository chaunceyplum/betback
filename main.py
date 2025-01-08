
from typing import Union
import json
import requests
from fastapi import FastAPI
from datetime import datetime, timedelta
import json
from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
from basketball_reference_scraper.teams import get_roster
import pandas as pd
import boto3

from scrape import scrape

app = FastAPI()


@app.get("/")
def read_root():
  return("Welcome to the betting API")

@app.get("/get_all_active_players")
async def get_all_active_players():
    # allPlayers = []
    # total_pages= 8
    # for page in range(1, total_pages):

    #     url = "https://nba-stats-db.herokuapp.com/api/playerdata/season/2023/?page="+str(page)              
    #     response = requests.get(url=url ).json()
    #     pagey = response["results"]
    #     for record in pagey:
    #         allPlayers.append(record)
    #     page += 1

    # return {"data": allPlayers}

    # df = get_roster('GSW', 2019)
    # print(df)
    
    return scrape()
   


@app.get("/get_player/{player_name}")
def get_player(player_name:str):
    url = "https://nba-stats-db.herokuapp.com/api/playerdata/name/" + player_name
    response = requests.get(url=url ).json()
    return response
