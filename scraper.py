import scrapy
import re
import time


class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://localhost:3000/test_login']
    base_url = "http://localhost:3000"
    quant = 0
    visited = []


    def parse(self, response):
        self.log(response.url)
        self.quant = self.quant + 1
        self.visited.append(response.url)
        # page = response.url.split("/")[-1]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # print(response.status)
        # for method in dir(response):
        #     print(method)
        s = '<a[^>]* href="([^"]*)"'
        pattern = re.compile(r'<a[^>]* href="([^"]*)"')

        for (link) in re.findall(pattern, str(response.body)):
            # print(link)
            # time.sleep(10)
            if link not in self.visited:
                self.visited.append(link)
                self.log(link)
                if link.startswith("http") == False:
                    link = self.base_url + link
                new_request = scrapy.Request(link)
                yield new_request
        # self.log('Crawled %s' % response.url)
        self.log(self.quant)
