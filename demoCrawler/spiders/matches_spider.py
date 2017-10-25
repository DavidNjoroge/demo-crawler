import scrapy

class MatchesSpider(scrapy.Spider):
    name='matches'
    start_urls=['http://www.stadiumastro.com/sports/epl/results-fixtures/week/10']

    def parse(self,response):
        for match in response.css('div.matchInfoBox'):
            yield{
        'home':match.css('span::text').extract_first(),
        'away':match.css('span::text').extract()[1]

        }
