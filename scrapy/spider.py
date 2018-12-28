import scrapy

class JournalSpider(scrapy.Spider):
    name = 'journalspider'
    start_urls = ['http://www.rondonopolis.mt.gov.br/diario-oficial/']

    def parse(self, response):
        for tr in response.css('.table-diary tr'):
            yield {'pdf': tr.css('a ::text').extract_first()}

        for next_page in response.css('a.page-link'):
            yield response.follow(next_page, self.parse)