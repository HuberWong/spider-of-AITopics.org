"""
# 使用说明

1. 修改需要收集资讯的页数 `page_number`，吃饭的时间搞就好
2. 运行本程序 `python3 main.py`
3. 将生成的 `AITopicsNews.csv` 文件用 Office Excel 或者 WPS 转成 `.xlsx` 格式
4. 如果英文看的慢的话，可以使用谷歌翻译整个文档
5. GOODLY

"""
page_number = 100
print(f'你将会获得 {page_number * 10} 条数据')

from newAITopicsSpider import NewAITopicsSpider

spider = NewAITopicsSpider()
spider.run(page_number)
