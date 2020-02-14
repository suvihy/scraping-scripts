import selenium
from selenium import webdriver
import pandas as pd
import numpy as np
import time
import csv

data = []
header_data = []

browser = webdriver.Firefox()
browser.get('https://www.bbc.co.uk/search?q=coronavirus&sa_f=search-product&scope=')


# This opens a new result page as long as there is results, now set to range 40.
# while True (ikuinen loop, kun taas for i in range voi tsekkaa tietyn määrän)
for i in range(1): 
    try:
        browser.find_element_by_class_name("more").click()
        time.sleep(1)
    except:
        break

# Following lines fetch the dates for articles
list_dates = browser.find_elements_by_tag_name("article time")

for date in list_dates:
    data.append(date.text) 
    print(date.text)

list_headers = browser.find_elements_by_tag_name("article h1") # get this one for news titles, you have to pay attention if you are fetching elementS or just one element

for header in list_headers:
    header_data.append(header.text)
    print(header.text)



# Following lines combines the data and convert the output to csv 
combined_data = list(zip(data, header_data))
df = pd.DataFrame(combined_data, columns=['date', 'title'])
export_csv = df.to_csv('results3.csv')
df.head()


""" table_content = "\n".join(df) # inside " " you put the delimiter, backslash + n puts the results in their own rows
f = open("result3.csv", "a")
f.write(df)
 """
#outputCSV = open('outputCSV.csv', 'a')
#with outputCSV:
            #writer = csv.writer(outputCSV)
            #writer.writerow(date.text) """

