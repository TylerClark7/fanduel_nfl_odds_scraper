Python script to scrape NFL odds from Fanduel.com

Selenium Scrapes https://sportsbook.fanduel.com/navigation/nfl for all pre playoff games

Returns a list of strings
Example String: 
MIN Vikings PHI Eagles +2 -105 +118 O 47.5 -110 -2 -115 -138 U 47.5 -110 SEP 19, 8:31PM ET Stats More wagers

sort_elem takes string and formats it into a dictionary
main.py returns a list of all dictionaries 


This should work for most NFL fanduel links where odds are displayed.
Currnetly only works for NFl stats becuase all nfl team names are a single word

At current state, certain fanduel games have "TOTAL" locked, these games cannot be scraped






