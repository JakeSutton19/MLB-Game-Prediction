import os
import pandas as pd


GAMES_PATH = "data/games/"
GAMES_SAVE_PATH = "data/GAMES_CSV/"


#Now lets loop through each file and convert it
#year = 2012


def Extract_Games_and_Save(Year):
	Team_LIST = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 
			 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SD', 'SF', 'SEA', 'STL', 'TB','TEX', 'TOR', 'WSN']

	for Team in Team_LIST:
		FILE_NAME = f"{GAMES_PATH}{Team}_{Year}"
		schedule_df = False
		
		try:
			schedule_df = pd.read_html(FILE_NAME)
		except:
			None
			
		if (schedule_df):
			games_table = schedule_df[4] #Games
		  
			#save path Write to csv
			table_path_1 = f"{GAMES_SAVE_PATH}{Team}_{Year}_games.csv"
			games_table.to_csv(table_path_1)


def Run_Games_Extract(YEARS):
	#Go through years
	#YEARS = list(range(2012, 2023))

	for Year in YEARS:
		Extract_Games_and_Save(Year)



def convert_win_streak(streak):
	if streak[0] == '+':
		return len(streak)
	else:
		return (-len(streak))

def convert_GB(gb):
	if gb[0] == 'u':
		gb = gb[2:]
		return float(gb)
	elif gb[0] == 'T':
		return 0
	else:
		return -float(gb)


def convert_outcome(outcome):
	if (outcome[0] == 'W'):
		return 1
	else:
		return 0

def convert_walkoff(outcome):
	if (outcome == 'W') or (outcome == 'L'):
		return 0
	else:
		if (outcome[0] == 'W'):
			return 1
		else:
			return -1


def convert_time_to_min(t):
	hour = t[0]
	min = t[2:]

	return ((int(hour)*60) + int(min))


def convert_day(x):
	if x == 'D':
		return 1
	else:
		return 0

def convert_night(x):
	if x == 'N':
		return 1
	else:
		return 0


def convert_date_to_datetime(day):
	if (day[-1] != ')'):
		return day[-6:]
	else:
		return day[-10:-4]


def convert_total_wins(record):
	return int(record.split('-')[0])

def convert_total_losses(record):
	return int(record.split('-')[1])



def clean_df(df):
	df['GameID'] = df['Gm#']
	df['Team'] = df['Tm']
	df['Outcome'] = df['W/L']
	df['W-L_record'] = df['W-L']
	df['Extra_Innings'] = df['Inn']
	df['Day-or-Night_g'] = df['D/N']
	df['champ_lev_index'] = df['cLI']
	df['Streaks'] = df['Streak'].apply(lambda x: convert_win_streak(x))
	
	del df['Orig. Scheduled']
	del df['Gm#']
	del df['Tm']
	del df['W/L']
	del df['W-L']
	del df['Inn']
	del df['D/N']
	del df['cLI']
	del df['Streak']
	del df['Unnamed: 0']
	del df['Unnamed: 2']
	del df['Unnamed: 4']
	del df['Win']
	del df['Loss']
	del df['Save']

	df = df[['Date', 'GameID', 'Team', 'Opp', 'Outcome', 'R', 'RA', 'W-L_record', 'Streaks', 'Rank', 'GB', 'Time', 'Attendance',
			   'Extra_Innings', 'Day-or-Night_g', 'champ_lev_index']]

	df = df[df.GameID != 'Gm#']

	return df




#FULL THING

def Process_Team_Schedules(Team, Year):
	GAMES_DATA_PATH = "data/GAMES_CSV/"

	file_string = f"{GAMES_DATA_PATH}{Team}_{Year}_games.csv"

	
	df = pd.read_csv(file_string) 
	
	df = clean_df(df)
	
	df['GB'] = df['GB'].apply(lambda x: convert_GB(x))
	
	df['Walkoff'] = df['Outcome']
	df['Outcome'] = df['Outcome'].apply(lambda x: convert_outcome(x))
	df['Walkoff'] = df['Walkoff'].apply(lambda x: convert_walkoff(x))
	df["Total_Innings"] = df['Extra_Innings'].fillna('9')
	del df['Extra_Innings']
	
	df['Time_Min'] = df['Time'].apply(lambda x: convert_time_to_min(x))
	del df['Time']
	
	df['is_day_game'] = df['Day-or-Night_g'].apply(lambda x: convert_day(x))
	df['is_night_game'] = df['Day-or-Night_g'].apply(lambda x: convert_night(x))
	del df['Day-or-Night_g']
	
	df['new_date'] = df['Date'].apply(lambda x: convert_date_to_datetime(x))
	
	test_dates = df['new_date']
	test_dates = pd.to_datetime(test_dates + ' ' + str(Year))
	
	df['y-m-d'] = test_dates
	del df['new_date']
	
	df['total_wins'] = df['W-L_record'].apply(lambda x: convert_total_wins(x))
	
	df['total_losses'] = df['W-L_record'].apply(lambda x: convert_total_losses(x))
	del df['W-L_record']
	
	del df['Date']
	
	df = df[['y-m-d', 'GameID',  'Time_Min', 'Team', 'Opp', 'R', 'RA', 'total_wins', 'total_losses',
					   'Total_Innings', 'Walkoff', 'Streaks', 'Rank', 'GB', 'Attendance', 'champ_lev_index', 'is_day_game', 'is_night_game', 'Outcome']]
	
	save_path = f"data/PROCESSED_GAMES/{Team}_{Year}.csv"
	df.to_csv(save_path)



#Now lets loop through 2012 games to see if it works

def Process_Teams(YEAR):
	Team_LIST = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KAN', 'LAA', 'LAD', 'MIA', 'MIL', 
				 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SD', 'SF', 'SEA', 'STL', 'TB','TEX', 'TOR', 'WSN']
	
	for Team in Team_LIST:
		Process_Team_Schedules(Team, YEAR)



def Run_Games_Cleaning(YEARS):
	#Now loop through all year files
	#YEARS = list(range(2012, 2023))

	for year in YEARS:
		Process_Teams(year)
