from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from sort import sort_elem
import pandas as pd
from IPython.display import display


stats = []
game_odds = []

options = Options()
options.headless = True
options.add_argument("--enable-javascript")

driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
# Can put almost any fanduel link here as long as it isolates nfl stats
driver.get("https://sportsbook.fanduel.com/navigation/nfl")

# driver.get("https://sportsbook.fanduel.com/navigation/nfl?tab=week-2")

# Returns all text for each block on https://sportsbook.fanduel.com/navigation/nfl
odds = driver.find_elements(
    By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div/div[3]/div/div')

for item in odds:
    # Selenium adds \n to each block of text
    stats.append(item.text.replace("\n", " "))

driver.quit()


# Element text returns 2 uneeded lines at front end end, [2:len(stats)-1] removes all 3
for stat in stats[2:len(stats)-1]:
    # Sometimes selenium returns headers like "NFL Odds"
    # this causes sort_elem to return None values
    # we dont want those

    stat_to_add = sort_elem(stat)
    if stat_to_add != None:
        game_odds.append(stat_to_add)

# This is just to visualise whats going on in terminal
for element in game_odds:

    df = pd.DataFrame(element)
    display(df)
    print("\n \n")

# Try week links like the one below
# URL = https://sportsbook.fanduel.com/navigation/nfl?tab=week-1
