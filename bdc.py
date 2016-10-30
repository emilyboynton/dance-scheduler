# from urllib import urlopen
import requests
# from selenium import webdriver
from bs4 import BeautifulSoup
from urlparse import urljoin
import datetime

date = datetime.date.today()
month = str(date.month)
day = str(date.day)

headers = {'User-Agent': 'Mozilla/5.0'}
url = "http://www.broadwaydancecenter.com/schedule/" + month + "_" + day + ".shtml"
response = requests.get(url, headers=headers)
bsObj = BeautifulSoup(response.content, "html.parser")

table = bsObj.find("table")

list_classes = []
rows = table.findAll("tr")

for row in rows:
	a_class = []
	details = row.findAll("td")
	if len(details) == 4:
		for detail in details:

	
			# THIS WORKS; KEEP TOGETHER:
			children = detail.findChildren()
			for child in children:
				if child.has_attr("href"):
					a_class.append([detail.text.encode('utf-8'), urljoin(url, child.get('href').encode('utf-8'))])
			if children == []:
				a_class.append(detail.text.encode('utf-8'))	
		list_classes.append(a_class)

print "HERE'S THE BREAK"

for each in list_classes:
	if each != []:	
		print each


	# for detail in details:
	# 	if detail.has_attr('href'):
	# 		print "have we even found anything?"
	# 		print detail.text

	# a_class = [each.text.encode('utf-8') for each in details if len(details) == 4]

# print response.status_code
# print response.headers
# print bsObj
# print table
# print count


# SAVE THIS:
	# if len(details) == 4:
	# 	for each in details:
	# 		a_class.append(each)
