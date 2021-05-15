import requests

url = "https://api.bilibili.com/x/space/arc/search"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}
params = {
    "mid": 387694560,
    "pn": 1,
    "ps": 25,
    "index": 1,
    "jsonp": "jsonp"
}
resp = requests.get(url,headers=headers,params=params)
js = resp.json()


infos = js['data']['list']['vlist']

bli = []
for info in infos:
    li = []
    author = info['author']
    bvid = info['bvid']
    pic = info['pic']
    title = info['title']

    li.append(author)
    li.append(bvid)
    li.append(pic)
    li.append(title)
    bli.append(li)

for ll in bli:
    print(ll)