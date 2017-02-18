# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class HomesSpider(scrapy.Spider):
    name = "homes"
    allowed_domains = ["homes.co.jp"]
    start_urls = [
        'http://www.homes.co.jp/chintai/tokyo/meguro-city/list/',
    ]

    def parse(self, response):
        """最初に行われる処理。ページングの各ページを抽出
        """
        soup = BeautifulSoup(response.body, "lxml")
        last_page_num = int(soup.find("li", class_="lastPage").text)

        for n in range(1, last_page_num + 1):
            yield scrapy.Request("{}?page={}".format(response.url, n), callback=self.parse_products)

    def parse_products(self, response):
        """1ページ分の処理。各部屋のリンクを抽出
        """
        soup = BeautifulSoup(response.body, "lxml")
        products: list(BeautifulSoup) = soup.find_all("td", class_="detail")
        for product in products:
            yield scrapy.Request(product.a.attrs["href"], callback=self.parse_product)

    def parse_product(self, response):
        """各部屋の処理、実際に保存する項目を抽出
        """
        print("#############")
        print(response.url)
        print("#############")
