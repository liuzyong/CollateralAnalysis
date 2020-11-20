import scrapy
from scrapyDemo.items import ScrapydemoItem


class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["jscq.com"]
    start_urls = ['http://www.jscq.com.cn/dsf/gq/jygg/index.html']

    def parse(self, response):
        item = ScrapydemoItem()
        res = response.xpath('//table/tr[@style="height:36px;"]')

        for r in res:
            td = r.xpath("td")
            item["name"] = td[1].xpath('./a/@title').extract_first().strip()

            item["floorPrice"] = td[3].xpath(
                "string(.)").extract_first().strip()

            item["type"] = td[2].xpath("string(.)").extract_first().strip()

            yield item
