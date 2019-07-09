import re

def parsing_url(url):
	regex_url=re.compile(r'(https?)://(www\.[A-Za-z]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
	res=regex_url.search(url)
	if res:
		print(res.group())
		print(res.groups())
		print(res.group(0))
		print(f"Protocol:{res.group(1)}")
		print(f"Domain:{res.group(2)}")
		print(f"Everything else:{res.group(3)}")
	else:
		return False

parsing_url("http://www.google.com")
parsing_url("https://www.google.com")
parsing_url("http://www.google.com/bio?q=random&word=find")
parsing_url("https://www.google.comabsfsghdjkfkf")
parsing_url("www.google.com")