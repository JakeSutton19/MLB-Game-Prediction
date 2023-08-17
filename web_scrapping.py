import os
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout
import time

#We need to grab seasons 2012 through 2022
SEASONS = list(range(2012,2023))


#Initialize where the data tables are going to be stored once they are scrapped.
DATA_DIR = "data"
TEAM_BATTING_DIR = os.path.join(DATA_DIR, "team_batting")
TEAM_FIELDING_DIR = os.path.join(DATA_DIR, "team_fielding")
TEAM_PITCHING_DIR = os.path.join(DATA_DIR, "team_pitching")
TEAM_SCHEDULE_DIR = os.path.join(DATA_DIR, "team_schedule")
SEASON_SUMMARY_DIR = os.path.join(DATA_DIR, "season_summary")
SEASON_STATS_DIR = os.path.join(DATA_DIR, "season_stats")
GAMES_DIR = os.path.join(DATA_DIR, "games")
WINS_ABOVE_AVG_POSITION_DIR = os.path.join(DATA_DIR, "wins_above_avg_position")


Season_Year = ""
Team_Name = ""

URL_1 = f"https://www.baseball-reference.com/leagues/majors/{Season_Year}.shtml"

URL_2 = f"https://www.baseball-reference.com/teams/{Team_Name}/{Season_Year}-schedule-scores.shtml"


#Function to scrape html from a webpage

async def get_html(url, selector, sleep=3, retries=10):
    html = None
    for i in range(1, retries+1):
        time.sleep(sleep * i)
        try:
            print(f"Scraping page. Attempt: {i}")
            async with async_playwright() as p:
                browser = await p.chromium.launch()
                page = await browser.new_page()
                await page.goto(url)
                print(await page.title())
                html = await page.inner_html(selector)
        except PlaywrightTimeout:
            print(f"Timeout error on {url}")
            continue
        else:
            break
    return html



#Scrape content from each mlb season stats page

async def scrape_single_season_stats(Season):
    
    URL_1 = f"https://www.baseball-reference.com/leagues/majors/{Season}.shtml"
   
    save_path = os.path.join(SEASON_STATS_DIR, URL_1.split("/")[-1])

    html = await get_html(URL_1, "#content")
    with open(save_path, "w+") as f:
        f.write(html)

    return "Completed"




async def scrape_season_stats(Seasons):

    for season in Seasons:
        URL_1 = f"https://www.baseball-reference.com/leagues/majors/{season}.shtml"
       
        save_path = os.path.join(SEASON_STATS_DIR, URL_1.split("/")[-1])
    
        html = await get_html(URL_1, "#content")
        with open(save_path, "w+") as f:
            f.write(html)

    return "Completed"



#Scrape content from each mlb game of season. Start with 2012 b/c miami marlines began then
Team_LIST = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KAN', 'LAA', 'LAD', 'MIA', 'MIL', 
             'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SD', 'SF', 'SEA', 'STL', 'TB','TEX', 'TOR', 'WSN']


# ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KAN', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SD', 'SF', 'SEA', 'STL', 'TB',
#Season = 2012


async def scrape_games(Team_list, Season):
    s_t = time.time()
    for team in Team_list:
        URL_2 = f"https://www.baseball-reference.com/teams/{team}/{Season}-schedule-scores.shtml"

        save_name = f"{team}_{Season}"
        save_path = os.path.join(GAMES_DIR, save_name)
    
        html = await get_html(URL_2, "#content")
        if (html):
            with open(save_path, "w+") as f:
                f.write(html)
    t = (time.time() - s_t)
    print(f"Completed. Total time: {t}")
    return True



def Perform_Web_Scrape_Games():
	
	SEASONS = list(range(2012,2017))

	for Season in SEASONS:
	    await scrape_games(Team_LIST, Season)