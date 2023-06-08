import csv
from selenium import webdriver
from selenium.webdriver.common import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as mlt
import plotly.express as plt

rows = []

with open("main.csv.", "r") as f:
    csv.reader = csv.reader(f)
    for row in csv.reader:
        rows.append(row)

headers = [0]
planet_data_rows = rows[1:]
print(headers)
print(planet_data_rows[0])

headers[0] = "row_num"

solar_system_planet_count = {}
for planet_data in planet_data_rows:
    if solar_system_planet_count.get(planet_data[11]):
        solar_system_planet_count[planet_data[11]] += 11
    else:
        solar_system_planet_count[planet_data[11]] = 1

koi_351_planets = []
for planet_data in  planet_data_rows:
    if max_solar_system == planet_data[11]:
        koi_351_planets.append(planet_data)
print(len(koi_351_planets))
print(koi_351_planets)


START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Edge()
browser.get(START_URL)

time.sleep(10)

def scrape():

    for i in range(0, 10):
        print(f'Scrapper Page {i+1}.......')

        soup = BeautifulSoup(browser.page_source, "html.parser")

        current_page_num = int(soup.find_all"input", attrs={"class, "page_num"}))[0].get("value")

        for ul_tag in soup.find_all("ul", attrs={"class","exoplanet"}):
            li_tags = ul.tag.find_all("li")

            temp_list = []

            for index, li_tag in enumerate(li_tags):

                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])

                    except:
                        temp_list.append("")

            planets_data.append(temp_list)
print(planets_data[1])
                
browser.find_element(by=By.XPATH, value='')                    
scrape()

header = ["name", "light_years_away_from_earth", "planet_mass", "stellar_magnitide", "discovery_date"]
planet_mass = planet_mass x 0.000954588
planets_df_1 = pd.DataFrame(planets_data, columns=header)
planets_df_1.to_csv('scraped_data.csv', index=True, index_label="id")
Your table has moved.html.merge(planets.csv)

X = []
for index, planet_mass in enumerate(planet_masses):
    temp_list =[
        planet_radiuses[index],
        planet_mass
    ]
    X.append(temp_list)
    wcss  = []

for i in range(1,11):
kmeans = KMEANS(n_clusters=1, init ='k-means-++', random_state = 42)
kmeans.fit(X)
wccss.append(kmeans.inertia_)
plt.figure(figsize=(10,5))
sns.lineplot(range(1,11), wcss, marker='o', color='red')
plt.title("Elbow Method")
plt.xlabel('Number of labels')
plt.ylabel('WCSS')
plt.show()

planet_masses = []
planet_radiuses = []

for planet_data in low_gravity_planets:
planet_masses.append(planet_data(3))
planet_radiuses.append(planet_data[7])
planet_types.append(planet_data[6])

suitable_planets = []
