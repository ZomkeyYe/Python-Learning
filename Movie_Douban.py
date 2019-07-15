# coding=utf-8
#一下程序用于实现爬取豆瓣电影排行榜信息
#lxml模块
from lxml import etree 
import requests
import io
import sys
import json
#为了解决有时候出现的乱码问题
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#从chrome检查-network中获取url和User-Agent
url = "https://movie.douban.com/chart" 
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
response = requests.get(url,headers=headers)#获取响应
info_str = response.content.decode('utf-8')#将响应内容解码
# print(info_str)

#使用lxml模块中的etree处理数据
info = etree.HTML(info_str)
print(info)

#需要把每部电影的信息组成一个字典,key为标题,url,图片地址,评论数,评分
ret1 = info.xpath("//div[@class='indent']/div/table")#每个table是一部电影
#print(ret1)
for table in ret1:
    item = {}

    #利用xpath helper从info中提取数据
    item["电影名"]=table.xpath(".//div[@class='pl2']/a/text()")[0].replace("/","").strip()
    item["地址"] =  table.xpath(".//div[@class='pl2']/a/@href")[0]
    item["图片"] = table.xpath(".//a[@class='nbg']/img/@src")[0]
    item["评价数"] = table.xpath(".//span[@class='pl']/text()")[0]
    item["评分"] = table.xpath(".//span[@class='rating_nums']/text()")[0]
    #print(item)

    #ensure_ascii=False是为了防止输出中文乱码，indent是缩进
    json_str = json.dumps(item, ensure_ascii=False,indent=4)
    
    with open('Movie_Douban.txt','a+') as f:#保存成文件
        f.write(json_str)
