import feapder


class AirSpiderTest(feapder.AirSpider):
    def start_requests(self):
        yield feapder.Request("https://www.baidu.com/s?wd=宁波旅行&pn=0")

    def parse(self, request, response):

        search_list = response.xpath('// *[ @ id = "1"]')
        for article in article_list:
            title = article.xpath("./text()").extract_first()
            url = article.xpath("./@href").extract_first()
            print(title, url)
        print(response)


if __name__ == "__main__":
    AirSpiderTest().start()