from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError
import os
from pathlib import Path
from html.parser import HTMLParser
import re

class TableParser(HTMLParser):
	def __init__(self):
	    HTMLParser.__init__(self)
	    self.in_td = False

	def handle_starttag(self, tag, attrs):
	    if tag == 'td':
	        self.in_td = True

	def handle_data(self, data):
	    if self.in_td:
	        print(data)

	def handle_endtag(self, tag):
	    self.in_td = False


website_name = "https://www.noosfere.org/livres/auteurpays.asp?numpays="

myfile = open("authors_test.txt", 'w+')

nb_pays = 0;
for i in range(100,1000):
	print("i: ",i)
	nb_pays = nb_pays + 1
	try:
		html_page = urllib.request.urlopen(website_name+str(i))
		soup = BeautifulSoup(html_page, "html.parser")
		for table in soup.find_all("a", href=re.compile("Auteur")):
			author = str(table.text)
			myfile.write(author+"\n")

	except HTTPError as err:
		print(err.code)

print("nombre de pays traités : ",nb_pays)