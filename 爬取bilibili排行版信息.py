from lxml import etree
import requests

# 要爬取的url，注意：在开发者工具中，这个url指的是第一个url
url = "https://www.bilibili.com/v/popular/rank/all"

# 模仿浏览器的headers
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}

# get请求，传入参数，返回结果集
resp = requests.get(url,headers=headers)
# 将结果集的文本转化为树的结构
tree = etree.HTML(resp.text)

# 定义列表存储所有数据
dli = []
# 遍历所有数据
for s in range(1,101):
    li = []
    #根据树的路径找到对应的数据集
    num = tree.xpath("/html/body/div[3]/div[2]/div[2]/ul/li["+str(s)+"]/div[1]/text()")  # 获取热搜排序
    name = tree.xpath("/html/body/div[3]/div[2]/div[2]/ul/li["+str(s)+"]/div[2]/div[2]/a/text()")# 获取标题
    url = tree.xpath("/html/body/div[3]/div[2]/div[2]/ul/li["+str(s)+"]/div[2]/div[2]/a/@href")#获取链接
    look = tree.xpath("/html/body/div[3]/div[2]/div[2]/ul/li["+str(s)+"]/div[2]/div[2]/div[1]/span[1]/text()")# 获取播放量
    say = tree.xpath("/html/body/div[3]/div[2]/div[2]/ul/li["+str(s)+"]/div[2]/div[2]/div[1]/span[2]/text()") # 获取评论量
    up = tree.xpath("/html/body/div[3]/div[2]/div[2]/ul/li["+str(s)+"]/div[2]/div[2]/div[1]/a/span/text()") # 获取up主
    score = tree.xpath("/html/body/div[3]/div[2]/div[2]/ul/li["+str(s)+"]/div[2]/div[2]/div[2]/div/text()") # 获取综合得分
    #获取数据集中的元素
    li.append(num[0])
    li.append(name[0])
    li.append(url[0])
    li.append(look[0])
    li.append(say[0])
    li.append(up[0])
    li.append(score[0])

    dli.append(li)
# 打印数据
for dd in dli:
    print(dd)