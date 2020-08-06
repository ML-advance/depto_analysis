import scrapy

from scrapping.items import Department


class ZoomSpider(scrapy.Spider):
    name = 'zoom'
    allowed_domains = ['zoominmobiliario.com']
    start_urls = ['https://www.zoominmobiliario.com/venta/departamento/usado/339-santiago?page=1']

    def parse(self, response):
        deptos = response.xpath('//div[@id="results"]/div')[1].xpath('//div[@class="container-button"]/a/@href')
        yield from response.follow_all(deptos, self.parse_depto)

        pagination_links = response.xpath('//li/a[@rel="next"]/@href')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_depto(self, response):
        depto = Department()
        depto['title'] = response.css('.nameProperty::text').extract_first()\
            .replace('\n', '').replace('\t', '').strip()
        depto['address'] = response.css('.address::text').extract_first()\
            .replace('\n', '').replace('\t', '').strip()
        depto['description'] = ''.join(response.css('.small-description div::text').extract())\
            .replace('\n', '').replace('\t', '').strip()
        depto['location'] = response.xpath('//h4[@id="locationent"]/@onclick').extract_first()\
            .replace("'", '').split(',')[1:]
        depto['price'] = response.css('.price-row1 .price-value::text').extract_first()\
            .replace('.', '')
        depto['currency'] = response.css('.price-row1 .price-type::text').extract_first()\
            .strip()
        depto['rooms'] = response.css('.list-inline-characteristics > li > .space::text')[1].extract()\
            .replace('\n', '').strip()
        depto['bathrooms'] = response.css('.list-inline-characteristics > li > .space::text')[3].extract()\
            .replace('\n', '').strip()
        depto['size_from'] = response.css('.list-inline-characteristics > li > .space::text')[5].extract() \
            .replace('\n', '').strip()
        depto['size_to'] = response.css('.list-inline-characteristics > li > .space::text')[6].extract() \
            .replace('\n', '').strip()
        depto['indicator'] = response.xpath('//img[@class="indicator"]/@title').extract_first()
        depto['url'] = response.request.url
        return depto
