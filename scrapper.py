import requests
from bs4 import BeautifulSoup

URL = 'https://www.nexusmods.com/skyrimspecialedition'

f = open(r'D:\Code\Python_Projects\Topics\Scrapper\results\results.txt', mode='w', encoding='utf-8')

page_html = requests.get(URL)     

page_soup = BeautifulSoup(page_html.content, 'html.parser')

mods_container = page_soup.find(id = 'mod-list')  # len(mods_container) = 5  -----  contains <div id = 'mod-list'> that table with all the mods on the page

mod_containers = mods_container.find_all('li', class_ = 'mod-tile') # len(mod_containers) = 20  ------ 20 mods shown on the page

i = 0

for k in mod_containers:  # for each of 20 mods do

	container_title = mod_containers[i].find('div', class_ = 'tile-content') 
	container_desc = container_title.p
	container_title = container_title.h3
	
	container_title = container_title.text.strip()
	container_desc = container_desc.text.strip()

	i += 1

	record = "--------------================= iteration " + str(i) + "=================----------------" + '\n' + '\n' + \
	'TITLE = ' + container_title + '\n' + 'DESCRIPTION = ' + container_desc + '\n' + '\n'
	f.write(record)
