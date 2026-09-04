import requests
import click
import re
from bs4 import BeautifulSoup

PAGE_URL = 'http://154.57.164.61:30936'

def get_html_of(url):
	req = requests.get(url)
	
	if req.status_code != 200:
		print(f'HTTP status code of {req.status_code} returned, but 200 was expected. Exiting...')
		exit(1)
	return req.content.decode()

def count_word(word_list, min_length):
	word_count = {}

	for word in word_list:
		if len(word) < min_length:
			continue
		if word not in word_count:
			word_count[word] = 1
		else:
			current_count = word_count.get(word)
			word_count[word] = current_count + 1
	return word_count
	
def get_all_words_from(url):

	html = get_html_of(PAGE_URL)
	soup = BeautifulSoup(html, 'html.parser')
	raw_text = soup.get_text()
	return re.findall(r'\w+', raw_text)

def get_top_words(all_words,min_length):
	word_count = count_word(all_words,min_length)
	return sorted(word_count.items(), key=lambda item: item[1], reverse=True)

@click.command()
@click.option('--url', '-u', prompt='Web URL', help='URL of webpage to extract from.')
@click.option('--length', '-l', default=0, help='Minimum word length(default: 0, no limit).')

def main(url, length):
	all_words = get_all_words_from(url)
	top_words = get_top_words(all_words, length)

	for i in range(10):
		print(top_words[i][0])

if __name__ == '__main__':
	main()
