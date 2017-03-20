# iSentia
###### News Crawl, Store and Search

### Crawl and Store
Crawl the news information from the news website stated in the config file and store data into compose mongodb:
> $ scrapy crawl iSentia

### Search
Search for article titles that contains the keyword supplied. <br />
Basically run the search_article function in the search_content.py with the keyword as input.<br />
Titles and urls of matching articles will be printed:
> search_article('Donald Trump')
