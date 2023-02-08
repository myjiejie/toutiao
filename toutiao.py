import requests
import execjs
import json
import time



o = {
    'url' : f'https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc'
}
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}

ctx = execjs.compile(open('sdk01.js',encoding='utf-8').read())
signature = ctx.call('get_sign',o)
min_time = int(time.time())

url = f'https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc&_signature={signature}'

resp = requests.get(url,headers=headers)
resp.encoding = "utf-8"
respjson = resp.json()
for item in respjson['data']:
    #print(item)
    title = item.get('Title')
    LabelDesc = item.get('LabelDesc')
    title_url = item.get('Url')
    #source = item['source']
    print(LabelDesc,',',title,'\n',title_url)
resp.close()

