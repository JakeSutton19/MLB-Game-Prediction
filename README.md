# MLB Game Prediction
Developed by Jacob Sutton, 2023

## Introduction
The goal of this project is to accurately predict the winner of MLB baseball games. 

The way I will test whether or not the system can accurately predict the winners of MLB baseball games is by testing the accuracy of the system against the 2023 season. The project will be continued by enabling the system to predict the winner of the 2023 World Series. The end result of the project is to be a interactive UI that allows a user to enter the details of a future game and find out who will win, and by what confidence. 



## Application
This is an interesting and useful solution. If accurate, the system could be used in a wide variety of applications within sports betting as well as by organizations to make better decisions. 




## Resources
I used several wonderful resources from DataQuest to compplete this project. Please see the list for references:
  
  - Web Scraping: https://www.youtube.com/watch?v=o6Ih934hADU&t=3904s&ab_channel=Dataquest
  - Data/ML:
        - 1) https://www.youtube.com/watch?v=ZO3HAVm9IdQ&ab_channel=Dataquest
        - 2) https://www.youtube.com/watch?v=0irmDBWLrco&ab_channel=Dataquest



## Setup 
* Expected Oct 2023



# Results
### WEEK 1: 
8/7-8/13

After the first week, I was able to scrape each team's schedule from 2012-2022 as well as their seasons statistics. I then cleaned the data and complied it into 2 files, one for games and one for team stats. I then created a simple Random Forrest to predict the outcome (1: W, 0: L). 


	- Error is 57.6%
	- Precision is 56.5%
	    - 0/0: 1189
	    - 0/1: 1241
	    - 1/0: 820
	    - 1/1: 1610
	
	
- 
