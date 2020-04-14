from bs4 import BeautifulSoup
import requests


	
r = requests.get('https://automatetheboringstuff.com/')

soup = BeautifulSoup(r.content, "lxml")

links = soup.find_all('a')
Chapters = []

for x in links:
	if 'Chapter' in x.text:
		Chapters.append(x.text)
text = []
for x in range(0, 21):
	r = requests.get('https://automatetheboringstuff.com/2e/chapter' + str(x) + '/')
	soup = BeautifulSoup(r.content, "lxml")
	text.append(soup.text)

for x in text:
	print(x)
