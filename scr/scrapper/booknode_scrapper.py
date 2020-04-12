from __future__ import print_function
from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError
import os
from pathlib import Path
from nameparser import HumanName
import time
import mechanize
import re
import time
import unidecode
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

myfile = open("/home/adrien/Documents/EBOOK_PROJET/calibre_clean_author/res.txt", 'w+')

def name_builder(name,name_rev):
	name = name.replace("-", " ") #remove - from name
	name = " ".join(name.split()) #remove extra blank space
	name = name.strip() #remove white space

	lastname = ""
	firstname = ""
	for i in range(0,len(name_rev)):
		current = (unidecode.unidecode(name_rev[i:i+2])).lower()
		if current == name[0:2]:
			firstname = name_rev[i:]
			break
		else:
			lastname = lastname+name_rev[i]

	if lastname == "":
		res = firstname.upper()
	else:
		res = lastname.upper()+" "+firstname.title()

	res = res.strip()
	res = " ".join(res.split())

	return res

def run():
	for l in letters:
		eprint("l: ",l)
		try:
			with open("/home/adrien/Documents/EBOOK_PROJET/calibre_clean_author/html/page_"+l+".html", 'r') as file:
				page_name = file.read()
				soup = BeautifulSoup(page_name, "html.parser")
				for info in soup.find_all("a", href=re.compile("https://booknode.com/auteur/")):
					author_name_rev = str(info.text)
					author_name = os.path.basename(os.path.normpath(info['href']))
					capitalized_author = name_builder(author_name,author_name_rev)
					myfile.write(capitalized_author+"\n")
					print(capitalized_author)
			file.close()
		except HTTPError as err:
			print(err.code)
		# time.sleep(1)

run()