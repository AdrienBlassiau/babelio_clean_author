from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError
import os
from pathlib import Path
from nameparser import HumanName
import time
import mechanize
import re
import codecs
import time
import sys

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
browser.open("https://booknode.com")
print(browser.title())
browser.select_form(nr = 4)
# print(browser.select_form(nr = 1))
browser.form['username'] = "mamezeho-4821"
browser.form['email'] = "mamezeho-4821@yopmail.com"
browser.form['password'] = "123456"
print(browser.form)
logged_in = browser.submit()
logincheck = logged_in.read()

# req = br.open("http://school.dwit.edu.np/mod/assign/").read()

# myfile = open("/home/adrien/Documents/EBOOK_PROJET/calibre_clean_author/babelio_scrapper.txt", 'w+')
# website_name = "https://www.babelio.com/auteur/William-R-Forstchen/"
# website_name_2 = "https://www.babelio.com/mesauteurs.php?id_user="

# authors_list = [134486,16837,92049,16943,15668,577210,336520,26,21061,11389,648426,389155,37983,69937,104809,618863,34579,165345,154619,67596,7908,231910,90714,92548,551596,361174,78745,66967,29552,521214,39885,25443,64192,98914,248965,22973,443903,111982,112632,444389,173222,14719,168045,69413,468360,472913,3962,72225,461071,150633,18400,101601,107843,40206,583191,40724,50238,62225,161846,99943,53943,53922,29519,53392,118089,112365,19604,253508,110196,113938,635110,19702,43303,159594,4381,151346,1408,29551,21083,70719,63764,329147,118048,714364,268239,38367,38348,42775,167876,1676,29628,35785,9096,28178,9263,327790,312938,877363,187383,294541,4382,434464,591577,48447,353118,47258,9263,107065,46049,181624,42891]

# def last_capitalizer(name):

# 	name = name.strip()
# 	name = " ".join(name.split())
# 	u_name = HumanName(name)

# 	if (u_name.first 	!= "" and
# 		u_name.title 	== "" and
# 		u_name.middle 	== "" and
# 		u_name.last 	== "" and
# 		u_name.suffix 	== ""):
# 	   return u_name.first.upper()

# 	last_name = u_name.last+" "+u_name.suffix
# 	u_name = last_name.upper()+" "+u_name.title+" "+u_name.first+" "+u_name.middle

# 	u_name = u_name.strip()
# 	u_name = " ".join(u_name.split())

# 	return u_name

# #2469
# def run1():
# 	for i in range(75801,75802):
# 		print("i: ",i)
# 		try:
# 			html_page = urllib.request.urlopen(website_name+str(i))
# 			soup = BeautifulSoup(html_page, "html.parser")
# 			# print(soup)
# 			author_name = (soup.title.string.split("- Babelio", 1)[0]).split(" (", 1)[0]
# 			capitalized_author = last_capitalizer(author_name)
# 			print(capitalized_author)
# 			if not "BABELIO -" in capitalized_author:
# 				myfile.write(capitalized_author+"\n")
# 			# time.sleep(1)
# 		except HTTPError as err:
# 			print(err.code)

# def run2():
# 	toolbar_width = len(authors_list)
# 	sys.stdout.write("[%s]" % (" " * toolbar_width))
# 	sys.stdout.flush()
# 	sys.stdout.write("\b" * (toolbar_width+1))

# 	for i in authors_list:
# 		# print("i: ",i)
# 		sys.stdout.write("-")
# 		sys.stdout.flush()
# 		try:
# 			html_page = browser.open(website_name_2+str(i)).read()
# 			soup = BeautifulSoup(html_page, "html.parser")
# 			# print(soup)
# 			for table in soup.find_all("a", href=re.compile("/bibliotheque.php")):
# 				author_name = str(table.text)
# 				# print(author_name)
# 				capitalized_author = last_capitalizer(author_name)
# 				# print(capitalized_author)
# 				if not "LIVRES "  in capitalized_author:
# 					myfile.write(capitalized_author+"\n")

# 		except HTTPError as err:
# 			pass
# 			# print(err.code)
# 	sys.stdout.write("]\n")

# run2()