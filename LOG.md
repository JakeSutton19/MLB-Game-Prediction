
# LOG


## Results

#### WEEK 1: 
8/7-8/13

After the first week, I was able to scrape each team's schedule from 2012-2022 as well as their seasons statistics. I then cleaned the data and complied it into 2 files, one for games and one for team stats. I then created a simple Random Forrest to predict the outcome (1: W, 0: L). 

- Error is 57.6%
- Precision is 56.5%
    - 0/0: 1189
    - 0/1: 1241
    - 1/0: 820
    - 1/1: 1610


## LOG Discussion

- It seems that in order to answer my general question of who will win, I should focus on predicting outcomes that have 
to do with the potential bets it could be used for:
	
	1. Moneyline
	2. Over/Under
	3. Runline
	4. W/L

So I will begin my focus on these statistics and use the base project from BP Tutorial as the foundation for my pipeline. 