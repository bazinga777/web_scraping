from bs4 import BeautifulSoup
import urllib2
 
wiki = "http://www.espncricinfo.com/ci/engine/match/index.html?view=live"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page,"lxml")

#print(soup.title)
#live=soup.find("section", {"id": "live-match-data"})
#print live



# following code extracts information about all live matches 
for link in soup.find_all('section',{'id':'live-match-data'}) :
#for link in soup.find_all('section',{'data-matchstatus':''}) :
	link_desc=link.descendants
	for d in link_desc:
		if d.name=='div' and d.get('class', '') == ['match-info']:
			print(d.text)
                     

			
			
	#bar=link.find_all('div',attrs={'class':'match-info'})
	#print bar.text
