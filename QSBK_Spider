# coding=utf-8
#导入需要使用的模块
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')#为了防止有时候输出产生中文乱码的问题
import requests
from lxml import etree
import json
class QSBK_Spider:
    def __init__(self):
        #url 和 User-Agent
        self.url_temp = "https://www.qiushibaike.com/{0}/page/{1}/"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

    def get_url_list(self): 
        #获取url地址规律,构造为list
        url_list = [self.url_temp.format(i,j) for i in ['text','hot','history'] for j in range(1,14)]
        return url_list

    def parse_url(self,url):
        #获取响应
        print("正在处理：",url)
        response = requests.get(url,headers=self.headers)
        return response.content.decode()

    def get_content_list(self,html_str):
        #利用lxml提取数据
        html = etree.HTML(html_str)
        #将提取的数据分组
        div_list = html.xpath("//div[@id='content-left']/div")
        # print(div_list)
        content_list = []
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
            content_list.append(info)
        return content_list

    def save_content_list(self,content_list):# 保存
        with open("QSBK_Spider.txt","a",encoding="utf-8") as f:
            for content in content_list:
                f.write("\n")
                f.write(json.dumps(content,ensure_ascii=False,indent=4).replace(' ',''))
                f.write("\n")
                f.write("\n")
                f.write("***********************************************************")
        print("保存成功")
    def run(self):
        #1.根据url地址的规律,构造url list
        url_list = self.get_url_list()
        #2.发送请求,获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            #3.提取数据
            content_list = self.get_content_list(html_str)
            #4.保存
            self.save_content_list(content_list)

if __name__ == '__main__':
    #实例化方法
    QSBK = QSBK_Spider()
    QSBK.run()
