#import packages 
import requests
import pandas as pd
from bs4 import BeautifulSoup

#Getting the page 
page = requests.get("https://www.pushsquare.com/guides/best-ps5-games")
page
page.status_code
page.content

#Create a BeautifulSoup object 
soup = BeautifulSoup(page.text, 'html.parser')

#Print Pretty 
print(soup.prettify())

# Get titles 
Names = soup.find_all('h3', class_="heading")
Names

Name_list = []

# clean data a little 

for i in Names:
    n = i.text
    n = n.strip()
    n = n.replace('\n','')
    n = n.replace(' ','')
print(i.text)
Name_list.append(i.text)

len(Name_list)
Name_list

# put into dataframe and get csv 
df = pd.DataFrame({'Playstation_Games':Name_list})

df.to_csv('data/PS5.csv')
