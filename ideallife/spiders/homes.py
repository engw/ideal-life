# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

from ideallife.items import IdeallifeItem


class HomesSpider(scrapy.Spider):
    name = "homes"
    allowed_domains = ["homes.co.jp"]
    start_urls = [
        'http://www.homes.co.jp/chintai/tokyo/shibuya_00578-st/list/',
        'http://www.homes.co.jp/chintai/tokyo/yoyogi_00580-st/list/',
        'http://www.homes.co.jp/chintai/tokyo/harajuku_00579-st/list/',
        'http://www.homes.co.jp/chintai/tokyo/ebisu_00577-st/list/',
        'http://www.homes.co.jp/chintai/tokyo/meguro_00576-st/list/',
        'http://www.homes.co.jp/chintai/tokyo/omotesando_06316-st/list/',
        'http://www.homes.co.jp/chintai/tokyo/gaiemmae_06315-st/list/',
        'http://www.homes.co.jp/chintai/tokyo/meijijingumae_06372-st/list/',
        'http://www.homes.co.jp/chintai/tokyo/yoyogikoen_06373-st/list/',
        'http://www.homes.co.jp/chintai/tokyo/nogizaka_06371-st/list/',
        'http://www.homes.co.jp/chintai/tokyo/hiro_06347-st/list/',
        'http://www.homes.co.jp/chintai/tokyo/kitasando_10052-st/list/',
        'http://www.homes.co.jp/chintai/tokyo/ikejiriohashi_05091-st/list/',
        'http://www.homes.co.jp/chintai/tokyo/sangenjiyaya_05092-st/list/',
        'http://www.homes.co.jp/chintai/tokyo/aoyamaitchome_06314-st/list/',
        'http://www.homes.co.jp/chintai/tokyo/daikanyama_05050-st/list/',
        'http://www.homes.co.jp/chintai/tokyo/nakameguro_05051-st/list/',
        'http://www.homes.co.jp/chintai/tokyo/shinsen_04974-st/list/',
        'http://www.homes.co.jp/chintai/tokyo/komabatodaimae_04975-st/list/',
    ]

    def parse(self, response):
        """最初に行われる処理。ページングの各ページを抽出
        """
        soup = BeautifulSoup(response.body, "lxml")
        last_page_num = int(soup.find("li", class_="nextPage").find_previous_sibling('li').text)
        for n in range(1, last_page_num + 1):
            yield scrapy.Request("{}?page={}".format(response.url, n), callback=self.parse_products)

    def parse_products(self, response):
        """1ページ分の処理。各部屋のリンクを抽出
        """
        soup = BeautifulSoup(response.body, "lxml")
        products = soup.find_all("td", class_="detail")
        for product in products:
            yield scrapy.Request(product.a.attrs["href"], callback=self.parse_item)

    def parse_item(self, response):
        """各部屋の処理、実際に保存する項目を抽出
        """
        soup = BeautifulSoup(response.body, "lxml")
        title = soup.find(id='chk-bkh-name').text
        rent = soup.find(id="chk-bkc-moneyroom").text
        deposit, tip = [x.strip() for x in soup.find(id="chk-bkc-moneyshikirei").text.split('/')]
        nearest_stations = [station for station in soup.find(id="chk-bkc-fulltraffic").text.split('\n') if station][:-1]
        address = soup.find(id="chk-bkc-fulladdress").contents[0].strip()
        birthday = soup.find(id="chk-bkc-kenchikudate").text
        window_angle = soup.find(id="chk-bkc-windowangle").text
        dimension = soup.find(id="chk-bkc-housearea").text.strip()
        layout = soup.find(id="chk-bkc-marodi").text.strip()

        return IdeallifeItem(url=response.url,
                             title=title,
                             rent=rent,
                             deposit=deposit,
                             tip=tip,
                             nearest_stations=nearest_stations,
                             address=address,
                             birthday=birthday,
                             window_angle=window_angle,
                             dimension=dimension,
                             layout=layout)
