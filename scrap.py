# In this project we are going to scrap data from a website (https://news.ycombinator.com/news)
import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')	#first news page
res2 = requests.get('https://news.ycombinator.com/news?p=2')  #second news page
soup = BeautifulSoup(res.text,'html.parser')
soup2 = BeautifulSoup(res2.text,'html.parser')	#for the second news page
# print(soup)	#show the whole file in html format
# print(soup.body)	# show the body part of the file
# print(soup.body.contents)	#show the whole content
# print(soup.find_all('div'))	#show the whole divs in the file
# print(soup.find_all('a'))	#show the whole a tags in the file
# print(soup.title)	#show the title of the website
# print(soup.a)	#show the first a tag
# print(soup.find('a'))	#show the first a tag
# print(soup.find(id='24488224'))
#using css selector
# print(soup.select('.score'))	#show all the span with the class="score"
# print(soup.select('#score_24488224')) #show the span with the specific score
# print(soup.select('.storylink')[0])	#show the first link (the class of every link is 'storylink')

links = soup.select('.storylink')
links2 = soup2.select('.storylink')	#for the second news page
# votes = soup.select('.score')	#instead of score class we are going to use subtext class for not getting error while we are getting points
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')	#for the second news page
# print(votes[0]) #show how many votes the first news have
# print(votes[0].get('id'))	#show the score of the first vote
mega_links = links+links2	#to combine the links in two pages
mega_subtext = subtext+subtext2	#to combine subtext in two pages
#the bellow function is used to sort the results
def sort_votes(hnlist):
	return sorted(hnlist, key=lambda k:k['votes'],reverse=True) #show the votes of each news in increase and decrese


def create_custom_hn (links,subtext):
	hn=[]
	for idx,item in enumerate(links):
		title = item.getText()	#title = links[idx].getText()
		# hn.append(title)	#add titles to hn list
		href = item.get('href',None)	#href = links[idx].get('href',None)
		# hn.append(href)
		votes = subtext[idx].select('.score')
		
		if len(votes):	#by adding this line we prevent the error (some news does not have votes)
			points = int(votes[0].getText().replace('points',' '))
			print(points)
			if points>99:	#just select news with more than 100 votes
				hn.append({'title':title, 'link':href, 'votes':points})	#we want to combine title and link
	# return hn
	return sort_votes(hn)
pprint.pprint(create_custom_hn(mega_links,mega_subtext))