import selenium
from selenium import webdriver
import time
import csv

data = []
header_data = []

browser = webdriver.Firefox()
browser.get('https://www.bbc.co.uk/search?q=coronavirus&sa_f=search-product&scope=')

for i in range(1): 
    try:
        browser.find_element_by_class_name("more").click()
        time.sleep(1)
    except:
        break

ol = browser.find_element_by_tag_name("ol.search-results")
list_articles = ol.find_elements_by_tag_name("li")

for art in list_articles:
    time = art.find_element_by_tag_name("time").text
    article = art.find_element_by_tag_name("h1").text
    line = time + ',' + article + '\n'
    print(line)

#solve this one still
df = lines
table_content = "\n".join(df) # inside " " you put the delimiter, backslash + n puts the results in their own rows
f = open("results.csv", "a")
f.write(df)



