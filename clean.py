from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError
import os
from pathlib import Path
from nameparser import HumanName
import time

myfile = open("/home/adrien/Documents/EBOOK_PROJET/cleaning_project/babelio_authors.txt", 'w+')
website_name = "https://www.babelio.com/auteur/William-R-Forstchen/"

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

#2469
def run():
	for i in range(2469,10000):
		print("i: ",i)
		try:
			html_page = urllib.request.urlopen(website_name+str(i))
			soup = BeautifulSoup(html_page, "html.parser")
			# print(soup)
			author_name = (soup.title.string.split("- Babelio", 1)[0]).split(" (", 1)[0]
			capitalized_author = last_capitalizer(author_name)
			print(capitalized_author)
			if not "BABELIO -" in capitalized_author:
				myfile.write(capitalized_author+"\n")
			# time.sleep(1)
		except HTTPError as err:
			print(err.code)

run()