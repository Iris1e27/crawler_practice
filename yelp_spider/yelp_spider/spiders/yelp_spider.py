from urllib.parse import urljoin

import scrapy

from yelp_spider.items import RestaurantItem


class YelpSpider(scrapy.Spider):
    name = 'yelp'
    start_urls = [
        'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Manhattan%2C+NY']
    next_start = 0

    # 添加headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.google.com",
        "Accept-Language": "en-US,en;q=0.9",
        # 添加其他你需要的header字段
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        # 使用提供的XPath表达式选择所有li[]元素
        elements = response.xpath('//*[@id="main-content"]/div/ul/li')
        number = self.next_start + 1

        for element in elements:
            name = element.xpath('.//h3/span[text()]/a/text()').get()  # [text()]可以用来过滤广告店铺
            if name is None: continue
            detail_url = element.xpath('.//h3/span/a/@href').get()
            address = element.xpath('.//div/p/span[2]/text()').get() or element.xpath(
                './/div/p/span[3]/text()').get()  # 有的没有$$所以是可能2或者3
            cuisine_tags = []
            cuisine_tag_elements = element.xpath(
                './/div/p/span[@class=" display--inline__09f24__c6N_k  border-color--default__09f24__NPAKY"]/a')
            for tag_element in cuisine_tag_elements:
                cuisine_tags.append(tag_element.xpath('.//button/span/text()').get())
            features = []
            # features_tag_elements = element.xpath('.//div[@class="  border-color--default__09f24__NPAKY nowrap__09f24__lBkC2"]')

            features_tag_elements = element.xpath(
                './/ul[@class=" undefined list__09f24__ynIEd"]/li/div/div')
            print("Features Tag Elements:", name, len(features_tag_elements))
            for tag_element in features_tag_elements:
                is_ok = '√ '
                icon = tag_element.xpath('./div/span/@class').get(default='')
                if icon and 'close' in icon: is_ok = '× '
                text = tag_element.xpath('./span/p/span/text()').get(default='')
                if text is not None:
                    feature = is_ok + text
                    self.logger.info(feature)
                    features.append(feature)

            rating = element.xpath('.//span[@class=" css-gutk1c"]/text()').get()
            price_range = element.xpath('.//div/p/span[2]/span/text()').get()
            reservation_link = element.xpath('.//div[@class="  border-color--default__09f24__NPAKY"]/a/@href').get()

            # 记录当前爬取的网站URL
            source_url = response.url
            reservation_link = urljoin(source_url, reservation_link)
            detail_url = urljoin(source_url, detail_url)

            item = RestaurantItem(
                name=name,
                detail_url=detail_url,
                address=address,
                cuisine_tags=cuisine_tags,
                rating=rating,
                features=features,
                price_range=price_range,
                reservation_link=reservation_link,
                source_url=source_url
            )

            yield item
            self.logger.info(f"爬取到第 {number} 条数据")
            print(f"爬取到第 {number} 条数据", number)
            number += 1

        self.next_start += 10

        # 检查是否还有下一页
        if self.next_start < 240:
            # 计算下一页的start值
            print('next start', self.next_start)
            # 构造下一页的URL
            next_page_url = f'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Manhattan%2C+NY&start={self.next_start}'

            # 发起新的请求继续爬取下一页
            yield scrapy.Request(next_page_url, headers=self.headers, callback=self.parse,
                                 meta={'start': self.next_start})
