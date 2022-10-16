
'''
# 使用说明

1. 修改需要收集资讯的数量 `numberOfNews`，最好是 10 的整倍数，因为每张页面上有10条资讯，时间为一周的话填 700 就差不多，吃饭的时间搞就好
2. 运行本程序 `python3 main.py`
3. 将生成的 `AITopicsNews.csv` 文件用 Office Excel 或者 WPS 转成 `.xlsx` 格式
4. 如果英文看的慢的话，可以使用谷歌翻译整个文档
5. GOODLUCK

'''
numberOfNews = 30

from AITopicsSpider import *

spider = AITopicsSpider()
spider.run(numberOfNews)