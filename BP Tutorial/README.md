# Baseball Prediction Tutorial from Numeristical


Tutorial from Numeristical: https://github.com/numeristical/resources/tree/master/BaseballPred

Youtube Series: https://www.youtube.com/playlist?list=PLeVfk5xTWHYCCqpcNlbRdIXi2CNt9zKvs



### BP 1:

- Scrape MLB game data from 1980 - 2022 from Retrosheet: https://www.retrosheet.org/gamelogs/index.html
- Create team dataframes and concat together
- End up with about 96K individual games
- Save to CSV file


### BP 2:

- Load in data from most recent CSV
- Train model with minmal batting features
	- Use LightBGM
	- Use StructureBoost


### BP 3:

- Add Las Vegas Odds for games 2018-2022
	- Scrape from OddShark: https://www.oddsshark.com/
- Load in CSV 
- Create dictionary to hold odds for games
- Iterate through data and add odds to rows
- Save to CSV file


### BP 4:
- Load in data from most recent CSV
- Train model with minmal batting features
	- Use LightBGM
	- Use StructureBoost

- Results show that LV odds are better than our current model
	- Largest discrepencies when we have strong pitcher vs weak pitcher
	- Means we need to factor in starting pitching


### BP 5:

- Add Pitcher data for games
	- Scrape all pitcher stats (3,015 total)
	- Data from Retrosheet: https://www.retrosheet.org/boxesetc/1

- Iterate through data and add starting pitcher data to rows
- Save to CSV file



### BP 6:

- Load in data from most recent CSV
- Train model with minmal batting features
	- Use LightBGM
	- Use StructureBoost


- Train model with minmal batting features + pitching features
	- Use LightBGM
	- Use StructureBoost


- Results show that imporovement but there is still work to be done
	- Adding bullpen data could improve results

### BP 7:

- Create bullpen features from current data set
	- Can subract starting pitching from total pitching performance to get 
	bullpen performance

- Save dataset as CSV


### BP 8:

- Load in data from most recent CSV

 - Train model with batting features + pitching features +
 bullpen features
	- Use LightBGM
	- Use StructureBoost

- Conculsions:
	- Still about 40 bps away from Vegas probabilities (down from about70)
	- When our model and Vegas "disagree", Vegas is generally right
	- We are running out of "big wins"
	- Features based on actual starting lineup
		- Fielding
		- Lefty vs Righty analysis


### BP 9:


### BP 10:


### BP 11:


### BP 12:


### BP 13:


### BP 14:


### BP 15:



