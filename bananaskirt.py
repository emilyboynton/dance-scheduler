from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

chromedriver = "/Users/emilyboynton/node_modules/chromedriver/lib/chromedriver/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

url = "https://clients.mindbodyonline.com/classic/home?studioid=176169"
driver.get(url)

driver.switch_to.frame(0)

s = driver.page_source
soup = BeautifulSoup(s, "lxml")

table = soup.find(id="classSchedule-mainTable")

inner_table = table.tbody


rows = inner_table.find_all('tr')

count = 0
dance_classes = []

for row in rows:
	dance_class = []
	data = row.find_all('td')
	for datum in data:
		no_nbsp = datum.text.replace(u'\xa0', u' ')
		final_data = no_nbsp.encode('utf-8').strip()
		if final_data == '':
			continue
		else:
			dance_class.append(final_data)
	dance_classes.append(dance_class)


for dance_class in dance_classes:
	print dance_class

# print inner_table.prettify()