# MLB Game Prediction

The goal of this project is to accurately predict the outcomes of MLB baseball games. The way I will test whether or not the system can accurately predict the winners and losers of mlb baseball games is by training the system on 10 years of games from 2012 - 2022 and then testing the accuracy of the system against the 2023 season. 

This project is being started midseason, in order to give a definite timeline of completeling the system and having a whole season of games to predict, in order to optimize the system to its fullest. 


This is an interesting and useful solution. If accurate, the system could be used in a wide variety of applications within sports betting as well as by organizations to make better decisions. 

This project is officially beginning on August 7th of 2023, with expectation to finish up by Sepetember 7th of 2023. The end result of the project is to be a interactive UI that allows a user to enter the details of a game and find out who will win, and by what confidence. 



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I used several wonderful resources from DataQuest to compplete this project. Please see the list for references:
  
  - Web Scraping: https://www.youtube.com/watch?v=o6Ih934hADU&t=3904s&ab_channel=Dataquest
  - Data/ML:
        - 1) https://www.youtube.com/watch?v=ZO3HAVm9IdQ&ab_channel=Dataquest
        - 2) https://www.youtube.com/watch?v=0irmDBWLrco&ab_channel=Dataquest


## WEEK 1 8/7-8/13

After the first week, I was able to scrape each team's schedule from 2012-2022 as well as their seasons statistics. I then cleaned the data and complied it into 2 files, one for games and one for team stats. I then created a simple Random Forrest to predict the outcome (1: W, 0: L). My current precision is 57.8%, with lots of room to improve the model. 
