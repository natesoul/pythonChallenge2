import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

url = "https://www.iban.com/currency-codes"

data = []
count = 0
select1 = ""
select2 = ""

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
            return
        else:
            print("You choose "+data[word-1][0])
            print("The currency code is "+data[word-1][2])
            return word-1
            
    except ValueError:
        print("that's not a number!")
        return

def exchange(): 
  try: 
    amount = int(input(f"How many {currency1} do you want to convert to {currency2} ?"))

    url = f"https://transferwise.com/gb/currency-converter/{currency1}-to-{currency2}-rate?amount={amount}"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    value = soup.find("input",{"class":"js-TargetAmount"})["value"]

    print(f"{currency1} {amount} is {currency2}", value)

    print(format_currency(value, currency2, locale="ko_KR"))
  except ValueError:
    print("that's not a number!")
    exchange()

collectData()

print("Welcome to CurrencyConvert Pro 2000\n")
count = len(data)
for i in range(count):
    print("# ", i+1, data[i][0])

while True:
  print("Where are you from? Choose a country by number")
  select1 = chooseCountry()
  if select1 != None:
    break

while True:
  print("Now Choose another country")
  select2 = chooseCountry()
  if select2 != None :
    break

currency1 = data[select1][2]
currency2 = data[select2][2]

exchange()