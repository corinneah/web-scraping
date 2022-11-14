#import packages 
import requests
import pandas as pd
from bs4 import BeautifulSoup

#Getting the page 
page = requests.get("https://www.zippia.com/tattoo-artist-jobs/demographics/")
page
page.status_code
page.content

#Create a BeautifulSoup object 
soup = BeautifulSoup(page.text, 'html.parser')

#Print Pretty 
print(soup.prettify())

# Get titles 
titles = soup.find_all('h2', class_="brandonH2 w-730 z-mb-48")
titles

title_names = []

# clean data a little 

for i in titles:
    t = i.text
    t = t.strip()
    t = t.replace('\n','')
    t = t.replace(' ','')
print(i.text)
title_names.append(i.text)

len(title_names)
title_names

# put into dataframe and get csv 
df = pd.DataFrame({'Tattoo_Stats':title_names})

df.to_csv('data/tattoo.csv')



