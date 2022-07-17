# Web Scraping
Web scraping is a technique used to grab data from a website saving lots of 
time and effort.

1. Inspect the website to see the HTML behind it.
2. In the code file, import necessary libraries.  These include, but are not 
   limited to requests, urllib.request, and beautifulsoup.
3. Set the url to the desired website and retrieve it using `requests.get(url)`.
4. Parse the code using `soup = BeautifulSoup(response.text, "html.parser")`.
5. Use `soup.findAll('\<tag>)` where tag can be any of the tags used in HTML.
6. Do what is desired with the information the tag retrieves.

##### Source: [How to Web Scrape with Python in 4 Minutes](https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460)

