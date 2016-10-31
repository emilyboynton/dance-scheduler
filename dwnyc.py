from bs4 import BeautifulSoup
import urllib
import re
import csv

r = urllib.urlopen('http://danceworksnewyorkcity.com/audition-results').read()
soup = BeautifulSoup(r, "html.parser")

all_dancers = []
tests = soup.find_all("div", class_= "sqs-block-content")
d = []
for test in tests:
	the_list = []
	p = test.find('p')
	if p:
		prev = test.find('p').previous_sibling
		next_ = test.find('p').next_sibling
		if (prev and next_):
			prev = prev.string.replace("\"", "").title()
			for each in next_:
				the_list.append(each.string)
		q = p.find_all(text=True, recursive=False)
		# print q[0]
		z = q[0].string.strip()
		if (q[-1] != q[0]):
			t = q[1].string.strip()
			if (t.split(',') != False):
				u = t.split(',', 1)
				if (u[0] != u[-1]):
					v = u[0].split(' ', 1)
					x = u[1].strip()
					d.append({"choreographer": z, "dance": prev, "date": v[0], "time": v[1], "room": x, "dancers": the_list })

for dict_ in d:
	# print dict_["choreographer"]
	# print dict_["dance"]
	# print dict_["date"]
	# print dict_["time"]
	# print dict_["room"]
	for dancer in dict_["dancers"]:
		# print dancer
		all_dancers.append(dancer.encode('utf-8'))

all_dancers.sort()
final_dancers = set(all_dancers)
print final_dancers

	