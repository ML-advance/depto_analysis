import scrapy
from scrapy.crawler import CrawlerProcess

from scrapping.items import Quote
from datetime import datetime


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    id = 0

    def parse(self, response):
        author_page_links = response.css('.author + a')
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)

    @staticmethod
    def extract_with_css(response, query):
        return response.css(query).get(default='').strip()

    def parse_author(self, response):
        quote = Quote()
        quote['id'] = self.id
        self.id = self.id + 1
        quote['name'] = self.extract_with_css(response, 'h3.author-title::text')
        quote['birthdate'] = self.extract_with_css(response, '.author-born-date::text')
        quote['bio'] = self.extract_with_css(response, '.author-description::text')
        quote['created_at'] = datetime.now().isoformat()
        return quote


if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(QuotesSpider)
    process.start()  # the script will block here until the crawling is finished
    print()
