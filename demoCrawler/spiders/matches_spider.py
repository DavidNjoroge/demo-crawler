import scrapy


class MatchesSpider(scrapy.Spider):
    name = 'matches'
    start_urls = ['http://www.stadiumastro.com/sports/epl/results-fixtures/week/10']

    def parse(self, response):
        for match in response.css('div.matchInfoBox'):
            yield {
                'home': match.css('span::text').extract_first(),
                'away': match.css('span::text').extract()[1]

            }
        next_page = response.css('#nextWeek::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
