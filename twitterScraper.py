import pandas as pd 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep, time
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


browser = webdriver.Chrome("/home/ubuntu/Downloads/chrome/chromedriver")
url = ["url1","url2"] # List of urls
l = []

for i in range(len(url)):
	try:
		browser.get(url[i])
		WebDriverWait(browser,20)
		d = {}

		d['handle'] = browser.find_element_by_xpath("//*[@class='ProfileHeaderCard-screenname u-inlineBlock u-dir']").text
		date = browser.find_element_by_xpath("//*[@class='ProfileHeaderCard-joinDate']").text.split(" ")[1:]
		d['date_of_joining'] = ",".join(date)


		a = browser.find_elements_by_xpath("//*[@class='ProfileNav-value']")
		d['tweets'] = a[0].text
		d['following'] = a[1].text
		d['followers'] = a[2].text
		d['likes'] = a[3].text

		l.append(d)

	except:
		print("Url not found")
		
df = pd.DataFrame(l)
df.to_csv("data.csv",header=False)

