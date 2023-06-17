# -*- coding: utf-8 -*-
"""ScrapeWiki.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kxZSXvV1nfoIkWW2yJKMm1ryF-bxq5wj
"""

#import our modules and packages that we will need to scrape a website
import csv
from bs4 import BeautifulSoup
import requests
import time
from google.colab import files

#grab every alphabetical list with our script
def scrape_content(url):
  time.sleep(2)
  #headers so server host can contact me if issues arise
  headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
              "from" : "wiki"}
  #open the website
  page = requests.get(url)
  page_content = page.content

  #parse the page with Beautiful Soup Library
  soup = BeautifulSoup(page_content, "html.parser") # contains html of whole webpage
  # print('this is what soup is', soup)
  content = soup.find("div", class_= "mw-content-ltr") #finds first tag with given class and sets equal to variable
  # print('this is what content is', content)
  all_groupings = content.find_all("div", class_= "mw-category-group") #all groupings is empty?? is that right?
  # print('this is what all_groupsings is', all_groupings)

  #make empty array for data
  rows = []

  # print('before the for loop works')
  for grouping in all_groupings:
    names_list = grouping.find("ul")
    category = grouping.find("h3").get_text()
    alphabetical_names = names_list.find_all("li")
    # print('hello')
    #create a row of information that contains the name, the link, and the letter connected to each name
    for alphabetical_name in alphabetical_names:
      #get name
      name = alphabetical_name.text
      #get the link
      anchortag = alphabetical_name.find("a", href = True)
      link = anchortag["href"]
      #get the letter
      letter_name = category
      #make a data dict that will be written into the csv
      row = {"name": name,
            "link": link,
            "letter_name": letter_name}
      rows.append(row)

#in case we pass multiple url perameters
# for url in urls:
#   scrape_content(url)

  #make a new csv into which we will write all the rows
  with open("all-women-computer-scientists.csv", "w+") as csvfile:
    #these are the header names
    fieldnames = ["name", "link", "letter_name"]
    #this creates your csv
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #this writes in the first row, which are the headers
    writer.writeheader()

    #loops through rows (the array I set at the beginning and have updated throughout)
    for row in rows: #nothing in rows right now ;/
    #takes each row and writes it into csv
      writer.writerow(row)

  download the CSV file
  files.download("all-women-computer-scientists.csv")

scrape_content("https://en.wikipedia.org/wiki/Category:Women_computer_scientists")