# coding:utf-8
import scrapy


class DouPanSpiders(scrapy.Spider):
    name = ""
    start_url = []

    def parse(self, response):
        yield response.xpath()