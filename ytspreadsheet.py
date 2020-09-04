import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from datetime import date
from info import user_data_path

today = str(date.today())  # gets today's date

options = webdriver.ChromeOptions()
options.add_argument(
    f"user-data-dir={user_data_path}")

path = 'C:\Program Files\chromedriver2.exe'
driver = webdriver.Chrome(options=options, executable_path=path)

driver.get('https://www.youtube.com/feed/history')
driver.maximize_window()

titles = driver.find_elements_by_id(
    'contents')[1].find_elements_by_id('video-title')
authors = driver.find_elements_by_id(
    'contents')[1].find_elements_by_class_name('style-scope ytd-channel-name')

data = {'Video Name': [],
        'Video Author': [],
        'Date Viewed': [today]*len(titles)}

for title in titles:
    data['Video Name'].append(title.text)

for index, author in enumerate(authors):
    if index % 2 == 0:
        data['Video Author'].append(author.text)

df = pd.DataFrame(data)
df.set_index('Date Viewed', inplace=True)
df.to_csv('ythistory.csv', mode='a')

driver.quit()
