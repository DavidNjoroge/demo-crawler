import scrapy


class QuotesSpider(scrapy.Spider):
    name='quotes'
    start_urls=[
    'http://quotes.toscrape.com/page/1/',
    'http://quotes.toscrape.com/page/2/',
    'https://simplefx.com/dashboard/'
    ]
    # url=['http://quotes.toscrape.com/page/1/']

    # def start_requests(self):
    #     urls=[
    #     'http://quotes.toscrape.com/page/1/',
    #     'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        # page=response.url.split('/')[-2]
        # filename='quotes-%s.html'% page
        # with open(filename,'wb') as f:
        #     f.write(response.body)
        # self.log('saved file %s' % filename)
        for quote in response.css('div.quote'):
            yield{
        'text': quote.css('span.text::text').extract_first(),
        'author': quote.css('small.author::text').extract_first(),
        'tags': quote.css('div.tags a.tag::text').extract(),
            }