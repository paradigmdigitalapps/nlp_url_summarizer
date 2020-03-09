# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
from text_summarizer import FrequencySummarizer
import requests

#it is importan to add header to request otherwise some ewbserver might reject the answer
#the will produce <head><title>403 Forbidden</title></head>
# e.g. 
# https://securityboulevard.com/2020/03/devsecops-the-best-security-strategy-in-2020/#respond
# such, and all errors when r.text is empty of server is not responding shall be handled with exeptions 
# 

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def getTextFromURL(url):
	r = requests.get(url, headers = headers)
	soup = BeautifulSoup(r.text, "html.parser")
	text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
	return text

def summarizeURL(url, total_pars):
	url_text = getTextFromURL(url).replace(u"Â", u"").replace(u"â", u"")

	fs = FrequencySummarizer()
	final_summary = fs.summarize(url_text.replace("\n"," "), total_pars)
	return " ".join(final_summary)

url = input("Enter a URL\n")
final_summary = summarizeURL(url, 5)
print(final_summary)