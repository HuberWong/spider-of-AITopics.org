from time import sleep
from fake_useragent import UserAgent
import requests
from lxml import etree

FILE = open('AITopicsNews.csv', 'w', newline='')

class AITopicsSpider(object):

    # 基本参数
    url = 'https://aitopics.org/search?start={}'

    # 需要爬取的条数

    # 性能参数

    def __init__(self):
        randomUserAgent = UserAgent
        self.headers = {
            'User-Agent': str(UserAgent().random)
        }

    def parseOnePageToSave(self, times):
        # TODO 修改 url
        # html = requests.get(url=self.url, headers=self.headers).text
        # html = open('./AITopicTest.html', 'r').read()
        html = requests.get(url=self.url.format(times), headers=self.headers).text
        print(self.headers)
        parsedHTML = etree.HTML(html)

        titleList = parsedHTML.xpath('//div/h3[@class="searchtitle"]/a/text()')
        linkList = parsedHTML.xpath('//div/h3[@class="searchtitle"]/a/@href')
        summaryContentList = parsedHTML.xpath('//div[@class="summary-content"]/p/text()')
        timeList = parsedHTML.xpath('//a/time/@datetime')

        # print(summaryContentList)
        for i in range(0, len(titleList)):
            n = News(titleList[i], linkList[i], summaryContentList[i], timeList[i])
            n.save()

    def run(self, numberOfPiecesOfData:int):
        for i in range(0, int(numberOfPiecesOfData / 10)):
            self.parseOnePageToSave(i)
            print('第' + str(i * 10) + '到' + str((i + 1) * 10) + '条资讯已经解析完毕')
            for j in range(4, 0, -1):
                print(str(j) + '秒结束后开始下次解析')
                sleep(1)

import csv


class News:
    file = FILE

    def __init__(self, t, l, s, ti):
        self.title = t
        self.link = l
        self.summaryContent = s
        self.time = ti

    def save(self):
        # with self.file as csvfile:
        #     csv.writer(csvfile).writerow([self.title, self.link, self.summaryContent, self.time])
        csv.writer(self.file).writerow([self.title, self.link, self.summaryContent, self.time])


if __name__ == '__main__':
    # 需要收集资讯的数量
    spider = AITopicsSpider()
    spider.run(30)
