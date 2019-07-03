# 用于爬取有道翻译，实现中英、英中翻译
import urllib.request
import urllib.parse
import json
def translate_auto(content):
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'#_o要去掉，否则会出先error_code:50的报错
    data={}
#i和doctype为必须键，否则影响翻译功能
    data['i']=content
    data['from']='AUTO'
    data['to']='AUTO'
    data['doctype']='json'
    data=urllib.parse.urlencode(data).encode('utf-8')
    response=urllib.request.urlopen(url,data)
    html=response.read().decode('utf-8')
    results=json.loads(html)
    #print(target)   查看results字典内容，从而确定打印方式
    print('翻译结果为(The result is):\n\t%s' %(results['translateResult'][0][0]['tgt']))
while True:
    content=input("请输入你想翻译的内容(按'q'随时退出)：\n")
    if content == 'q' or content == 'Q':
        break
    else:
        translate_auto(content)
