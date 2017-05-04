#!/usr/bin/python
# coding:utf-8


'''
Run this script with command 'python run.py'
'''


import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())
# Your spiders
process.crawl('all')
process.crawl('test')
process.start()  # the script will block here until the crawling is finished
