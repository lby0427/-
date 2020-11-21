import requests
from lxml import etree
import os
if __name__ == "__main__":
    url = 'https://baijiahao.baidu.com/s?id=1668256617617193651&wfr=spider&for=pc'
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    # param = {
    #     'query': 'python',
    #     'city': '101010100',
    #     'industry': '',
    #     'position': '',  # 从库中的第几部电影去取
    #
    # }
    response = requests.get(url=url, headers=headers)
    # response.encoding = 'utf-8'
    page_text = response.text



    #数据解析：src的属性值  alt属性
    tree = etree.HTML(page_text)
    p_list=tree.xpath('//*[@id="article"]/div/p//text()')
    p=''.join(p_list)
    #li_list = tree.xpath('//*[@id="main"]/div/div[2]/ul/li')
    print(p)
