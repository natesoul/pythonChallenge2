import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

data = []
count = 0

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
country = soup.find("tbody").find_all("tr")


def collectData():
    for i in country:
        r = i.find_all("td")
        group = []
        for q in r:
            group.append(q.text)
        if group[2] != "":
            data.append(group)


def chooseCountry():
    word = input("# : ")
    try:
        word = int(word)
        if word > count:
            print("Choose number from the list.")
            chooseCountry()
        else:
            print("You choose "+data[word-1][0])
            print("The currency code is "+data[word-1][2])
            chooseCountry()
    except:
        print("that's not a number!")
        chooseCountry()


collectData()

print("Hello! Please choose select a country number:")
count = len(data)
for i in range(count):
    print("# ", i+1, data[i][0])

chooseCountry()
