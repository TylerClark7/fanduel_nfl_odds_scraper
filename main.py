from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from sort import sort_elem

stats = []
n = []

options = Options()
options.headless = True
options.add_argument("--enable-javascript")

driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
driver.get("https://sportsbook.fanduel.com/navigation/nfl")
#driver.get("https://sportsbook.fanduel.com/navigation/nfl?tab=week-2")

#Returns all text for each block on https://sportsbook.fanduel.com/navigation/nfl
odds = driver.find_elements(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div/div[3]/div/div')

for item in odds:
    stats.append(item.text.replace("\n", " "))  #Selenium adds \n to each block of text                              

driver.quit()


for stat in stats[2:len(stats)-1]:
    #Element text returns 2 uneeded lines at front end end, [2:len(stats)-1] removes all 3
    n.append(sort_elem(stat))

#This is just to visualise whats going on in terminal
for el in n:
    print(el)
    print("\n")



#Try week links like the one below
#URL = https://sportsbook.fanduel.com/navigation/nfl?tab=week-1

