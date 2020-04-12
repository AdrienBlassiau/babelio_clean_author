from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError
import os
from pathlib import Path

def download_file(url,file_name):
	base_name = os.path.basename(file_name)
	trunc_base_name = Path(file_name).stem
	# print("extension :",os.path.splitext(file_name)[1])
	trunc_extension = os.path.splitext(file_name)[1]
	trunc_base_name = trunc_base_name[1:251]
	# print("truncated name: ",trunc_base_name)
	urllib.request.urlretrieve(url, "caron/"+trunc_base_name+trunc_extension)

website_name = "http://pa.caron.free.fr/plateforme/book/_catalog/book/"

visited = 0
total = 0

for i in range(0,6000):
	visited = 0
	print("i: ",i,"total =",total)
	try:
		html_page = urllib.request.urlopen(website_name+"book_"+str(i)+".html")
		soup = BeautifulSoup(html_page, "html.parser")
		for link in soup.findAll('a'):
		    file_adress = link.get('href')
		    if file_adress != None and (file_adress.endswith('.epub') or file_adress.endswith('.mobi') or file_adress.endswith('.pdf') or file_adress.endswith('.lrf') or file_adress.endswith('.azw3') or file_adress.endswith('.azw') or file_adress.endswith('.txt') or file_adress.endswith('.cbz') or file_adress.endswith('.cbr') or file_adress.endswith('.kcc')):
		    	visited = visited + 1
		    	if visited == 1:
		    		total = total+1
		    	total_file_adress = website_name+file_adress
		    	print(total_file_adress)
		    	download_file(total_file_adress,file_adress)
	except HTTPError as err:
		print(err.code)


## ftp://162.253.154.138/books/_catalog/index.html
