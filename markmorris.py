from bs4 import BeautifulSoup
from urllib import urlopen
import re

list_classes = []
url = "http://markmorrisdancegroup.org/dance-center/adult-classes/"
html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")

class_styles = bsObj.find_all("div", {"class":"schedule"})
for style in class_styles:
	children = style.findChildren()
	for child in children:
		if child.has_attr('href'):
			new_url = child.get('href')
			print new_url
			new_html = urlopen(new_url)
			new_bsObj = BeautifulSoup(new_html, "html.parser")

			results = new_bsObj.find_all("div", {"class":"class-group collapsed"})
			for result in results:
				something = 'C'
				level = 'Open'
				h = result.find("h2", {"class": "title"}).text.encode('utf-8')
				lv = re.search(r'(Beginning)|(Beg./Int.)|(Beg.)|(Advanced)|(Adv.)|(Intro to)|(Intro)|(Intermediate)|(Int./Adv.)|(Int.)|(Open Level Teen)|(Open Level)|(Open)', h)
				if lv:
					level = lv.group().encode('utf-8')
					class_style = h.replace(level, '').strip()
					h = class_style
				
				wk = re.search(r'(MMDG Series)|(Guest Series)|(Series)|(Workshop)', h)
				if wk:
					something = wk.group().encode('utf-8')
					final_class = h.replace(something, '').strip()
					h = final_class
				print h, level, something
				
				sc = result.find("div", {"class": "schedule"})
				if sc:
					det = result.find_all("td")
					class_details = []
					for d in det:
						ins = re.search(r'(Instructor:)|(Instructors:)|(Instructor)', d.text)
						if ins:
							# to account for any number of instructors per class
							mult_ins = d.find_all('a')
							for each in mult_ins:
								class_details.append(each.text.encode('utf-8'))
								class_details.append(each.get('href').encode('utf-8'))

						window = re.search(r'((January)|(February)|(March)|(April)|(May)|(June)|(July)|(August)|(September)|(October)|(November)|(December))( \d?\d)?(\s*-\s*((January)|(February)|(March)|(April)|(May)|(June)|(July)|(August)|(September)|(October)|(November)|(December))( \d?\d)?)?', d.text)			
						if window:
							if d.find('script'):
								break
							w = window.group().encode('utf-8').strip()
							final_w = ' '.join(w.split())
							class_details.append(final_w)

						dt = re.search(r'[((Mon)|(Tues)|(Wednes)|(Thurs)|(Fri)|(Satur)|(Sun))day \d?\d:\d\d[aAmMpP\.]* - \d?\d:\d\d[aAmMpP\.]*', d.text)
						if dt:
							class_details.append(dt.group().encode('utf-8').strip())
					print class_details

