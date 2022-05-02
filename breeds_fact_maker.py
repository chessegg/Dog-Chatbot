from urllib.request import urlopen
from bs4 import BeautifulSoup
import json


with open('breed_urls.json') as breed_list:
    breed_url_dict = json.load(breed_list)
breed_info_dict = {}

# for breed in breed_url_dict:
#print("Currently scraping info on " + breed)
breed_info_dict["Pembroke Welsh Corgi"] = {}
url = breed_url_dict["Pembroke Welsh Corgi"]
html = urlopen(url).read()
print(html)
soup = BeautifulSoup(html, "html.parser")

# colors
colors = soup.find("table", {"class": "accordion-toggle"})
print(colors)
for row in colors:
    print(row)
    color = row.find("td").text
    print(color)
    breed_info_dict["Pembroke Welsh Corgi"]['colors'] += [color]

# markings
# markings = soup.find(
#     "div", {"id": "accordion-markings"})
# for row in markings:
#     cells = row.find_all("td")
#     marking = cells[0].get_text()
#     breed_info_dict["Pembroke Welsh Corgi"]['markings'] += [marking]


with open("breed_facts.json", "w") as outfile:
    json.dump(breed_info_dict, outfile, indent=4)
