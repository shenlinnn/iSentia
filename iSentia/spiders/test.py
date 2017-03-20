import scrapy
from mercury_parser import ParserAPI
from iSentia.items import IsentiaItem
from iSentia.config import api_key, domains, urls

class myspider(scrapy.Spider):
    name = "iSentia"
    allowed_domains = domains
    start_urls = urls

    def parse(self, response):
        ## primary sections have class = 'global-navigation__title'
        ## by adding '/all' to each url to get all news under the section for all days
        ## call parse_dir_contents parser to crawl the news url
        for sel in response.xpath("//a[@class='global-navigation__title']"):
            url = sel.xpath('@href').extract()[0] + '/all'
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        ## news are located in div with class = 'fc-item__container'
        ## get each news url and call parse_article_contents parser
        ## recursive for maximum total 50 pages
        for sel in response.xpath("//div[@class='fc-item__container']"):
            url = sel.xpath('a/@href').extract()[0]
            yield scrapy.Request(url, callback=self.parse_article_contents)
        next = response.xpath("//a[@rel='next']/@href")
        next_page = response.xpath("//a[@rel='next']/@data-page")
        if next:
            if int(next_page.extract()[0]) <= 50 :
                next_url = next.extract()[0]
                yield scrapy.Request(next_url, self.parse_dir_contents)

    def parse_article_contents(self, response):
        ## crawl the news information and store data into item
        item = IsentiaItem()
        ## article content is crawled from <p>
        content_block = response.xpath("//div[@class='content__article-body from-content-api js-article__body']/p/text()")
        content = ""
        ## to concat all content in <p>
        for p in content_block:
            content = content + " " + p.extract()
        item['content'] = content
        item['link'] = response.url

        ## article author and title is from mercury parser API
        mercury = ParserAPI(api_key=api_key)
        p = mercury.parse(response.url)
        item['author'] = p.author
        item['title'] = p.title
        ## parse the item to pipeline
        #yield item
        print item








