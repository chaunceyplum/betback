
from basketball_reference_scraper.teams import get_roster
import pandas as pd
import boto3


def scrape():
 team_list =[{"team":"Atlanta Hawks","abbreviation":"ATL"},{"team":"Boston Celtics","abbreviation":"BOS"},{"team":"Brooklyn Nets","abbreviation":"BKN"},{"team":"Charlotte Hornets","abbreviation":"CHA"},{"team":"Chicago Bulls","abbreviation":"CHI"},{"team":"Cleveland Cavaliers","abbreviation":"CLE"},{"team":"Dallas Mavericks","abbreviation":"DAL"},{"team":"Denver Nuggets","abbreviation":"DEN"},{"team":"Detroit Pistons","abbreviation":"DET"},{"team":"Golden State Warriors","abbreviation":"GSW"},{"team":"Houston Rockets","abbreviation":"HOU"},{"team":"Indiana Pacers","abbreviation":"IND"},{"team":"LA Clippers","abbreviation":"LAC"},{"team":"Los Angeles Lakers","abbreviation":"LAL"},{"team":"Memphis Grizzlies","abbreviation":"MEM"},{"team":"Miami Heat","abbreviation":"MIA"},{"team":"Milwaukee Bucks","abbreviation":"MIL"},{"team":"Minnesota Timberwolves","abbreviation":"MIN"},{"team":"New Orleans Pelicans","abbreviation":"NOP"},{"team":"New York Knicks","abbreviation":"NYK"},{"team":"Oklahoma City Thunder","abbreviation":"OKC"},{"team":"Orlando Magic","abbreviation":"ORL"},{"team":"Philadelphia 76ers","abbreviation":"PHI"},{"team":"Phoenix Suns","abbreviation":"PHX"},{"team":"Portland Trail Blazers","abbreviation":"POR"},{"team":"Sacramento Kings","abbreviation":"SAC"},{"team":"San Antonio Spurs","abbreviation":"SAS"},{"team":"Toronto Raptors","abbreviation":"TOR"},{"team":"Utah Jazz","abbreviation":"UTA"},{"team":"Washington Wizards","abbreviation":"WAS"}]

 df = pd.DataFrame(team_list)

 player_list = pd.DataFrame()
 for team in team_list:
  raw_player = get_roster(team["abbreviation"],2025)
  player_df = pd.DataFrame(raw_player)
  player_df["TEAM"] = team["abbreviation"]

  merged_df = pd.concat([player_list, player_df])
  player_list = merged_df

 s3_client = boto3.client('s3')
 player_list.to_csv('players_.csv',index=False)
 response = s3_client.upload_file('players_.csv', 'arn:aws:s3:us-east-1:129579558702:accesspoint/access', 's3://baisleylake/airflow/players.csv')
 # player_list.to_csv('s3://baisleylake/NBA/players.csv', index=False)
 return response
scrape()