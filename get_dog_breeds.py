from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

my_url = 'https://www.akc.org/dog-breeds/'
html = urlopen(my_url).read()

soup = BeautifulSoup(html, "html.parser")
# soup = soup.find(
#    'div', class_="mobile-select-menu__title")


# breeds_html = soup.findAll("div", {"class": "option"})
breeds_html = soup.select('option[value]')
# print(breeds_html)
breed_dict = {}
breeds = []

for breed_line in breeds_html:
    breed = breed_line.text
    breeds.append(breed)
    # print(breed)
    url = breed_line.get('value')
    breed_dict[breed] = url

with open("breed_list_extra.txt", "w") as outfile:
    json.dump(breeds, outfile, indent=4)
