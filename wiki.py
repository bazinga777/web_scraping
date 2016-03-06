from bs4 import BeautifulSoup
import urllib2
 
wiki = "http://en.wikipedia.org/wiki/List_of_postcode_districts_in_the_United_Kingdom"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page,"lxml")
 
soup.head
soup.title 