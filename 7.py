import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"
jobs =[]
count=0

def extract_jobs(company, link):
  if "http" not in link:
    link = alba_url+link
  r = requests.get(link)
  soup = BeautifulSoup(r.text, "html.parser")
  job =[]
  check = soup.find("div",{"id":"NormalInfo"})
  if check != None:
    result = soup.find("tbody")
    if result != None :
      result = result.find_all("tr")
      for i in result:
        location = i.find("td",{"class":"local first"})
        title = i.find("td", {"class":"title"})
        time = i.find("td", {"class":"data"})
        pay = i.find("td", {"class":"pay"})
        timeStamp = i.find("td",{"class":"regDate last"})
        if location != None: 
          location = location.text.replace("\xa0"," ")
        if title != None:
          title = title.find("span",{"class":"company"}).text
        if time != None:
          time = time.text
        if pay != None:
          if pay.find("span",{"class":"number"}) != None:
            pay = pay.find("span",{"class":"number"}).text
        if timeStamp != None:
          timeStamp = timeStamp.text
        # print(location, company, time, pay, timeStamp)
        if location != None:
          job = [location, title, time, pay, timeStamp]
      jobs.append(job)
      # print(job)
      # print(jobs)
      exporter (company)

def exporter (company):  
  # print("company", company)
  if company != None:
    print(f"saving ... {company}")
    company = company.replace("/", ",")
    # print(company, jobs)
    file = open(f"{company}.csv", mode="w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow (["Place", "Title", "Time", "Pay", "Date"])
    writer.writerows(jobs)
 
r = requests.get(alba_url)
soup = BeautifulSoup(r.text, "html.parser")
company = soup.find("div", {"id":"MainSuperBrand"}).find("ul", {"class":"goodsBox"}).find_all("li")[:-2]

for i in company:
  if i.find("span",{"class":"company"}) != None:
    company = i.find("span",{"class":"company"}).text
    link = i.find("a")["href"]
    count += 1
    print("Now Scrapping Job ... ", count)
    print(company, link)
    extract_jobs(company, link)
    print("\n")
print("Done...")