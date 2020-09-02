import scrapy
from call_rate.items import CallRateItem
from scrapy.selector import Selector


class CallSpider(scrapy.Spider):
    name = "call"
    
    def start_requests(self):
        # 수집해야할 url 리스트
        urls = []
        for i in range(1, 559): #559
            urls.append("https://finance.naver.com/marketindex/interestDailyQuote.nhn?marketindexCd=IRR_CALL&page="+str(i))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        item = CallRateItem()

        #날짜 수집
        dates = response.xpath('/html/body/div/table/tbody/tr/td[1]/text()').getall()
        #콜금리 수집
        callrates = response.xpath('/html/body/div/table/tbody/tr/td[2]/text()').getall()
        
        for item in zip(dates, callrates):
            callrate_info = {
                'date' : item[0].strip(),
                'callrate' : item[1].strip(),
            }

            yield callrate_info