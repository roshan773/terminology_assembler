from bs4 import BeautifulSoup
import requests, time
from googlesearch import search


'''
from googlesearch import search

search(query, tld='.co.in', lang='en', num=10, start=0, stop=None, pause=2.0)

* query = query
* tld = domain we want to search ex: '.co.in'
* lang = language
* num = searches for 10 different similar webpages in each and every websites
* start = first link we need to search (start=3, stop=6, will retrive the 3rd 4th and 5th links)
* pause = pause time between each search
'''


file_name = input("Input the file name: ")

with open(file_name, 'r') as file:
	queries = file.readlines()

file_1 = open(file_name[:-4]+'_with_definitions.txt', 'w')
#opening a new text file to add the definitions

for query in queries:
	print('\n'+query[:-1])
	# the last character is new line
	
	search_result = search('wiki '+query, num=1, stop=1)
	url = search_result.__next__()
	print(url+'\n')
	# search_result is a generator and .__next__() method is used to fetch the element in the generator
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	for p in soup.find_all('p'):
		# Certain first paragraphs in wiki contains empty string or a junk character
		# This takes care of skipping that paragraph 
		if p.text.__len__() > 5:
			paragraph = p.text
			# once found a paragraph with text, breaking the loop
			break

	print(paragraph)
	file_1.write(query[:-1] + ':  ' + paragraph + '\n')

file_1.close()
