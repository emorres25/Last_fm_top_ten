import urllib2
from bs4 import BeautifulSoup
import os

stdurl = "https://www.last.fm/music/"
band = raw_input("Enter the name of the band: ").split(' ')

furl = stdurl
for part in range(0,len(band)):
	if(part==len(band)-1):
		furl = furl + band[part]
	else:
		furl = furl + band[part] + '+'

print furl + "\n"

res = urllib2.urlopen(furl)

page = res.read()

splitted_page = page.split("<thead class=\"sr-only\">", 1)
splitted_page = splitted_page[1].split("</thead>", 1)
splitted_page = splitted_page[1].split("</tbody>", 1)

soup = BeautifulSoup(splitted_page[0], 'html5lib')
#print soup.prettify()
os.system('cls')
print """ -------------------------------------------------------------------------------
			THE TOP TRACKS OF THE BAND ARE:
 -------------------------------------------------------------------------------
		  """	
i=1
for parts in soup.find_all('a', class_="link-block-target"):
	this = parts.get('title')
	print str(i) + '. ' + str(this)
	i+=1
	