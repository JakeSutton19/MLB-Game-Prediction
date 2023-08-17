import os
import pandas as pd
from bs4 import BeautifulSoup




TEAM_STATS_PATH = "data/season_stats/"
TEAM_STATS_SAVE_PATH = "data/TEAM_STATS/"
YEARS = list(range(2012, 2023))

#Now lets loop through each file and convert it
#year = 2012

def Extract_Data_Tables(year):
    FILE_NAME = f"{TEAM_STATS_PATH}{year}.shtml"
    Season_stats = open(FILE_NAME, 'r')
    season_stats_df = pd.read_html(Season_stats)
    
    ss_table1 = season_stats_df[0] #Postseason
    ss_table2 = season_stats_df[1] #Batting
    ss_table3 = season_stats_df[2] #Pitching
    ss_table4 = season_stats_df[3] #Wins Above
    ss_table5 = season_stats_df[4] #Fielding
    
    #save path
    table_path_1 = f"{TEAM_STATS_SAVE_PATH}{year}_postseason.csv"
    table_path_2 = f"{TEAM_STATS_SAVE_PATH}{year}_batting.csv"
    table_path_3 = f"{TEAM_STATS_SAVE_PATH}{year}_pitching.csv"
    table_path_4 = f"{TEAM_STATS_SAVE_PATH}{year}_wins_above.csv"
    table_path_5 = f"{TEAM_STATS_SAVE_PATH}{year}_fielding.csv"
    
    #Write to csv
    ss_table1.to_csv(table_path_1)
    ss_table2.to_csv(table_path_2)
    ss_table3.to_csv(table_path_3)
    ss_table4.to_csv(table_path_4)
    ss_table5.to_csv(table_path_5)




def Run_Stat_Extraction(YEARS):

	for year in YEARS:
	    Extract_Data_Tables(year)



#Function to process each of the season stat files

def Process_Stat_Files(year):
    #Initialize Files
    b_file = f"data/TEAM_STATS/{year}_batting.csv"
    p_file = f"data/TEAM_STATS/{year}_pitching.csv"
    f_file = f"data/TEAM_STATS/{year}_fielding.csv"
    s_file = f"data/FULL_TEAM_DATA/{year}_full_stats.csv"

    #Perform batting clean
    batting = pd.read_csv(b_file)

    batting['players_used'] = batting['#Bat']
    batting['runs_scored'] = batting['R']

    del batting['Unnamed: 0']
    del batting['#Bat']
    del batting['R']

    batting = batting[['Tm', 'players_used', 'BatAge', 'R/G', 'G', 'PA', 'AB', 'runs_scored', 'H', '2B', '3B', 'HR', 'RBI',
       'SB', 'CS', 'BB', 'SO', 'BA', 'OBP', 'SLG', 'OPS', 'OPS+', 'TB', 'GDP',
       'HBP', 'SH', 'SF', 'IBB', 'LOB']]

    #Perform pitching clean
    pitching = pd.read_csv(p_file)

    pitching['pitchers_used'] = pitching['#P']
    pitching['runs_allowed'] = pitching['R']
    pitching['hits_allowed'] = pitching['H']
    pitching['hr_allowed'] = pitching['HR']
    pitching['walks_allowed'] = pitching['BB']
    pitching['int_wlk_allowed'] = pitching['IBB']
    pitching['hbp_allowed'] = pitching['HBP']
    pitching['pitch_so'] = pitching['SO']
    pitching['pitch_LOB'] = pitching['LOB']

    del pitching['#P']
    del pitching['R']
    del pitching['H']
    del pitching['HR']
    del pitching['BB']
    del pitching['IBB']
    del pitching['HBP']
    del pitching['SO']
    del pitching['LOB']
    del pitching['G']

    #Merge two df
    merged_data = pd.merge(batting, pitching, how='inner', on='Tm')

    #Perform fielding clean
    fielding = pd.read_csv(f_file)  

    fielding['def_chances'] = fielding['Ch']
    
    del fielding['G']
    del fielding['GS']
    del fielding['CG']
    del fielding['Inn']
    del fielding['Ch']

    #Merge rest
    merged_data = pd.merge(merged_data, fielding, how='inner', on='Tm')

    #Drop second to last row and save
    merged_data.at[32, 'Tm'] = "Totals"
    merged_data = merged_data.drop([31])
    merged_data.to_csv(s_file, index=False)



def Run_Stat_Cleaning(YEARS):
	#Small script to run through files
	for year in YEARS:
	    Process_Stat_Files(year)