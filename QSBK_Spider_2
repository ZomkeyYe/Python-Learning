# coding=utf-8
#导入需要使用的模块
#import itertools  
import urllib
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')#为了防止有时候输出产生中文乱码的问题
import requests
from lxml import etree
import json
count_1=1
count_2=1
#url 和 User-Agent
url = "https://www.qiushibaike.com/imgrank/page/{}/"#爬取含有图片的糗事百科
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
piccc = [] #初始化图片列表
content_list = [] #初始化内容列表
url_list = [url.format(i) for i in range(1,14)]#url地址的构建
#获取url地址规律,构造为list

for url in url_list:
        #获取响应
    print("正在处理：",url)
    response = requests.get(url,headers=headers)
    ttt = response.content.decode()
        #利用lxml提取数据
    html = etree.HTML(ttt)
        #将提取的数据分组
    div_list = html.xpath("//div[@id='content-left']/div")
        # print(div_list)    
  
    for div in div_list:
        info = {}
        info["用户"] = div.xpath(".//h2/text()")[0].strip() if len(div.xpath(".//h2/text()"))>0 else None
        info["内容"] = div.xpath(".//div[@class='content']/span/text()")
        info["内容"] = [i.strip().replace(" ", "") for i in info["内容"]]
        info["好笑"] = div.xpath(".//span[@class='stats-vote']/i/text()")
        info["好笑"] = info["好笑"][0] if len(info["好笑"])>0 else None
        info["评论"] = div.xpath(".//span[@class='stats-comments']//i/text()")
        info["评论"] =  info["评论"][0] if len(info["评论"])>0 else None
        info["图片地址"] = div.xpath(".//div[@class='thumb']//img/@src")
        info["图片地址"] = "https:"+info["图片地址"][0] if len(info["图片地址"])>0 else None
        #将字典内容附加到content_list
        #print(info["图片地址"])
        content_list.append(info)
        #将图片地址附加到piccc
        piccc.append(info["图片地址"])

for picsss in piccc:
    print(picsss)
    urllib.request.urlretrieve(picsss,'D:/code/QSBK3/'+str(count_1)+'.jpg')
    count_1+=1
with open("D:/code/QSBK_Spider_1.txt","a",encoding="utf-8") as f:
    for content in content_list:
        f.write("\n")
        f.write(" ("+str(count_2)+").  ")
        f.write(json.dumps(content,ensure_ascii=False,indent=4).replace(' ',''))
        f.write("\n")
        f.write("\n")
        f.write("***********************************************************")
        count_2+=1
print("保存成功")

