from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError
import os
from pathlib import Path
from nameparser import HumanName
import time
from html.parser import HTMLParser
import re
import codecs

# sort babelio_authors_2.txt | uniq -u > bab_res.txt

myfile = open("/home/adrien/Documents/EBOOK_PROJET/cleaning_project/babelio_authors_2.txt", 'w+')
# print(page_name.read())

def last_capitalizer(name):

	name = name.strip()
	name = " ".join(name.split())
	u_name = HumanName(name)

	if (u_name.first 	!= "" and
		u_name.title 	== "" and
		u_name.middle 	== "" and
		u_name.last 	== "" and
		u_name.suffix 	== ""):
	   return u_name.first.upper()

	last_name = u_name.last+" "+u_name.suffix
	u_name = last_name.upper()+" "+u_name.title+" "+u_name.first+" "+u_name.middle

	u_name = u_name.strip()
	u_name = " ".join(u_name.split())

	return u_name

#4580
def run():
	try:
		with codecs.open("/home/adrien/Documents/EBOOK_PROJET/cleaning_project/html_pages/res.html", 'r',encoding="windows-1252") as file:
			page_name = file.read()
			soup = BeautifulSoup(page_name, "html.parser")
			for table in soup.find_all("a", href=re.compile("https://www.babelio.com/auteur/")):
				author_name = str(table.text)
				# print(author_name)
				capitalized_author = last_capitalizer(author_name)
				print(capitalized_author)
				if not "BABELIO -" in capitalized_author:
					myfile.write(capitalized_author+"\n")
		file.close()
	except HTTPError as err:
		print(err.code)
	# time.sleep(1)

run()