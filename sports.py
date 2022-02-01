# Importing Necessary dependencies
import requests
from bs4 import BeautifulSoup
import csv

# Write data to a csv file
output_file = csv.writer(open('premier_table.csv', 'w+'))

# Adding headers to our CSV data
output_file.writerow(['Position', 'Team', 'Played',
 'Won', 'Drawn', 'Lost', 'For', 'Against', 'GD', 'Points'])

# Using requests to create a get-request from the target-url
url = "https://www.bbc.co.uk/sport/football/tables"
result = requests.get(url)
# print(result) # => This should print <Response [200]> for success

src = result.content
# print(src) # -> This prints the entire HTML page (source-code)

# Beautiful Soup 4 parsing HTML
soup = BeautifulSoup(src, 'html.parser')
# print(soup)

# Find table tag
table = soup.find_all("table")
league_table = table[0]

# under table rows for the information we need
teams = league_table.find_all("tr")

# Since they are 20 teams in EPL
for team in teams[1:21]:

    # Stats undert td-table data after inspection
    stats = team.find_all("td")

    # get the different team stats
    position = stats[0].text
    team_name = stats[2].text
    played = stats[3].text
    won = stats[4].text
    drawn = stats[5].text
    lost = stats[6].text
    for_goals = stats[7].text
    against_goals = stats[8].text
    goal_diff = stats[9].text
    points = stats[10].text

    # Write to our csv file we created earlier
    output_file.writerow([position, team_name, played, won,
               drawn, lost, for_goals, against_goals, goal_diff, points])
