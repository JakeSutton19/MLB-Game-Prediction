import pandas as pd 



def Check_Missing_Files():
	GAMES_PATH = "data/games/"
	GAMES_DATA_PATH = "data/GAMES_CSV/"

	TEAMS = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KAN', 'LAA', 'LAD', 'MIA', 'MIL', 
	                 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SD', 'SF', 'SEA', 'STL', 'TB','TEX', 'TOR', 'WSN']
	YEARS = list(range(2012, 2023))

	for team in TEAMS:
	    for year in YEARS:
	        
	        file_string = f"{GAMES_DATA_PATH}{team}_{year}_games.csv"

	        try:
	            f = open(file_string, 'r')
            	df = pd.read_html(f)

	        except:
	            print(f"File missing: {file_string}")

	print("Done")




def Check_Missing_Seasons():
	for team in TEAMS:
   		season_counter = 0
	    seasons = []
	    
	    for year in YEARS:
	        
	        file_string = f"{GAMES_DATA_PATH}{team}_{year}_games.csv"

	        try:
	            df = pd.read_csv(file_string) 
	            season_counter+=1

	        except:
	            seasons.append(year)

	    if season_counter < 11:
	        #print(f"{team} Season Files Count: {season_counter}")
	        print(f"{team} Missing Seasons: {seasons}\n")
	    

	print("Done")



def All_Team_Seasons_Count():
	#And now lets check our counts for each team
	GAMES_DATA_PATH = "data/GAMES_CSV/"


	for team in TEAMS:
	    season_counter = 0
	    
	    for year in YEARS:
	        
	        file_string = f"{GAMES_DATA_PATH}{team}_{year}_games.csv"

	        try:
	            
	            df = pd.read_csv(file_string) 
	            season_counter+=1

	        except:
	            None

	   
	    print(f"{team} Season Files Count: {season_counter}")
	        

	print("Done")



GAMES_DATA_PATH = "data/PROCESSED_GAMES/"

def Merge_Team_Seasons(Team):
    concated_df = pd.DataFrame()
    
    Years = list(range(2012, 2023))
    
    for year in Years:
        file_string_1 = f"{GAMES_DATA_PATH}{Team}_{year}.csv"
        df1 = pd.read_csv(file_string_1) 
        del df1['Unnamed: 0']
        concated_df = pd.concat([concated_df, df1], axis=0)
        save_string_1 = f"data/TEAM_SEASONS/{Team}_2012-2022.csv"
        concated_df.to_csv(save_string_1, index=False)

    print(f"Wrote: {Team}")



def Run_All_Merges():
	#Now write loop to do this for all teams

	TEAMS = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 
	             'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SD', 'SF', 'SEA', 'STL', 'TB','TEX', 'TOR', 'WSN']

	for team in TEAMS:
	    Merge_Team_Seasons(team)



def Merge_All_Games():
	GAMES_DATA_PATH = "data/TEAM_SEASONS/"

	TEAMS = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 
	             'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SD', 'SF', 'SEA', 'STL', 'TB','TEX', 'TOR', 'WSN']


	concated_df = pd.DataFrame()
	    
	for team in TEAMS:
	    file_string_1 = f"{GAMES_DATA_PATH}{team}_2012-2022.csv"
	    df1 = pd.read_csv(file_string_1) 
	    
	    concated_df = pd.concat([concated_df, df1], axis=0)
	    
	    save_string_1 = f"data/TEAM_SEASONS/TOTAL_TEAM_SEASONS_2012-2022.csv"
	    concated_df.to_csv(save_string_1, index=False)

	print("Done")