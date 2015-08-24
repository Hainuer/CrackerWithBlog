#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup

article_li = []

for idx in range(1, 4):
	if idx == 1:
		req = requests.get('http://www.hainuer.com')
		soup = BeautifulSoup(req.text, 'html.parser')
		for article in soup.find_all('article'):
			# h1 class="entry-title"
			article_info = article.find('h1', attrs={'class': 'entry-title'}).find('a')
			article_li.append({
				'title': article_info.get('title'),
				'link': article_info.get('href')
			})
	else:
		req = requests.get('http://www.hainuer.com/page/' + str(idx) + '/')
		soup = BeautifulSoup(req.text, 'html.parser')
		for article in soup.find_all('article'):
			# h1 class="entry-title"
			article_info = article.find('h1', attrs={'class': 'entry-title'}).find('a')
			article_li.append({
				'title': article_info.get('title'),
				'link': article_info.get('href')
			})

nums = len(article_li)
for article in article_li:
	nums = nums - 1
	print('Remain: ' + str(nums) + '\nCracker Start: ' + article['link'])
	req = requests.get(article['link'])
	soup = BeautifulSoup(req.text, 'html.parser')
	body = soup.find('div', attrs={'class': 'entry-content clearfix'})

	with open(os.path.join('/Users/Phoenix/Desktop/BlogArticles/', article['title'] + '.txt'), 'w+') as fi:
		fi.write('Title: ' + article['title'] + '\n')
		fi.write('Link:  ' + article['link'] + '\n\n')
		fi.write('Plaintext:\n' + body.get_text() + '\n\n')
		fi.write('Body:\n' + str(body) + '\n\n')

	print('Cracker  Stop: ' + article['link'])






