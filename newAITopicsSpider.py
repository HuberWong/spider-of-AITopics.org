import csv
import datetime
import random
import ssl
from time import sleep
from fake_useragent import UserAgent
import requests
from lxml import etree

FILE = open('newAITopicsSpider.csv', 'w+', newline='', encoding='utf-8')
LOG_FILE = open('log.txt', 'w+', newline='', encoding='utf-8')

class NewAITopicsSpider:
    url = 'https://aitopics.or/search?start={}'

    def __init__(self):
        self.headers = {
            'User-Agent': str(UserAgent().random),
            # 'Referer': 'https://aitopics.org/search'
        }

    def parseOnePageToSave(self, page_number):
        try:

            self.headers = {
                'User-Agent': str(UserAgent().random)
            }
            # TODO 修改 url
            # html = requests.get(url=self.url, headers=self.headers).text
            # html = open('./AITopicTest.html', 'r').read()
            # print(f'正在下载第{page_number}页')
            LOG_FILE.write(f'{str(datetime.datetime.now())}正在下载第{page_number}页\n')
            html: str
            if page_number == 0:
                html = requests.get(url='https://aitopics.or/search').text
            else:
                html = requests.get(url=self.url.format(page_number * 10), headers=self.headers).text
            # print(self.headers)
            parsedHTML = etree.HTML(html)

            titleList = parsedHTML.xpath('//div/h3[@class="searchtitle"]/a/text()')
            linkList = parsedHTML.xpath('//div/h3[@class="searchtitle"]/a/@href')
            summaryContentList = parsedHTML.xpath('//div[@class="summary-content"]/p/text()')
            timeList = parsedHTML.xpath('//a/time/@datetime')

            # print(summaryContentList)
            for i in range(0, len(titleList)):
                # print(titleList[i])

                n = News()
                n.title = titleList[i]
                n.link = linkList[i]
                n.summaryContent = summaryContentList[i]
                n.time = timeList[i]

                # print(f'正在保存第{page_number}页-第{i}条')
                LOG_FILE.writelines(f'正在保存第{page_number}页-第{i}条\n')
                n.save()
        except requests.exceptions.SSLError as e:
            waitTime = random.randint(1, 2)
            print('发生了一下错误\n' + str(e) + f'\n\n\n在 {waitTime}s 后将会重新尝试解析第 {page_number} 页')
            self.parseOnePageToSave(page_number)

    def run(self, times:int):
        for i in range(0, times + 1):
            self.parseOnePageToSave(i)
            waitTime = random.randint(5, 10)
            # if waitTime == 5:
            #     waitTime = random.randint(66,77)
            sleep(waitTime)
            print(f'在 {waitTime}s 后开始下载下一页')


class News:
    file = FILE

    title: str
    link: str
    summaryContent: str
    time: str

    def save(self):
        csv.writer(self.file).writerow([
            self.title,
            self.link,
            self.summaryContent,
            self.time
        ])


if __name__ == '__main__':
    s = NewAITopicsSpider()
    s.run(2)
