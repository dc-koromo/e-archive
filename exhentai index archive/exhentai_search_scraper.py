import requests
import time
import random


#anons need to fill this out with their cookies and page range before running.
#vpns are your friend.
page_range = range(0,3500)
cookies = dict(
	lv='',
	igneous='',
	s='',
	ipb_member_id='',
	sk='',
	ipb_pass_hash=''
)


s = requests.Session()
s.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}

#ensure proper page load
def loadExhPage(url):
	r = s.get(url, cookies=cookies).text
	if "<title>ExHentai.org</title>" in r:
		print("fetch success")
		return r
	if "Your IP address has been temporarily banned" in r:
		print(r)
		exit()
	print("fetch fail: " + r)
	return loadExhPage(url)

#main loop
for i in page_range:
	fname = "exhentai_page_"+str(i+1)+".html"
	print("fetching page " + str(i+1))
	f=open(fname,"w+", encoding='utf8')
	url = "https://exhentai.org/?page="+str(i)
	f.write(loadExhPage(url))
	f.close()
	print("wrote file " + fname)
	#time.sleep(1)
