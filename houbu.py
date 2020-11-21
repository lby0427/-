from selenium import webdriver
from time import sleep
import requests
from lxml import etree
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    url = 'https://bingli.iiyi.com/dept/8-3.html'
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
   # ['/html/body/div[5]/div[1]/div[1]/ul[1]/li[1]/a[2]']
    li_list = tree.xpath('/html/body/div[5]/div[1]/div[1]/ul/li')
    all_url = []
    b=[]
    for li in li_list:
        new_url = li.xpath('./a[2]/@href')[0]

        #new_page_text = requests.get(url=new_url, headers=headers).text
        #new_tree = etree.HTML(new_page_text)
        #context=new_tree.xpath('/html/body/div[5]/div[1]/div[4]/div[1]/p/text()')


        all_url.append(new_url)
    print(all_url)

    # for index in all_city_names :
    #     new_page_text = requests.get(url=new_url, headers=headers).text
    #     new_tree = etree.HTML(new_page_text)
    #     context = new_tree.xpath('/html/body/div[5]/div[1]/div[4]/div[1]/p/text()')
    #     print(context)



# bro.switch_to.frame('login_frame')
#
# a_tag = bro.find_element_by_id("switcher_plogin")
# a_tag.click()



try:
    bro = webdriver.Chrome(executable_path='./chromedriver')
    bro.get('https://account.iiyi.com/')
    userName_tag = bro.find_element_by_id('username')
    password_tag = bro.find_element_by_id('password')
    sleep(1)
    userName_tag.send_keys('15150661019')
    sleep(1)
    password_tag.send_keys('zh123456')
    sleep(1)
    btn = bro.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/form/input')
    btn.click()
    sleep(3)
    # bro.get('https://s.iiyi.com/tnav?site=bbs&0.023098404402442263')
    # sleep(3)
    n=0
    for i in all_url:
        bro.get(('%s')%i[0])
        for li in bro.find_elements_by_xpath('/html/body/div[5]/div[1]/div[1]'):
            title = li.find_element_by_xpath('./h1').text
            print(title)
        for li in bro.find_elements_by_xpath('/html/body/div[5]/div[1]/div[4]/div[1]'):
            content1 = li.find_element_by_xpath('./p').text
            print(content1)
            #['/html/body/div[5]/div[1]/div[2]/div[1]/p']
        for li in bro.find_elements_by_xpath('/html/body/div[5]/div[1]/div[2]/div[1]'):
            content = li.find_element_by_xpath('./p').text
            print(content)
        sleep(2)
        n+=1
        print('-------------------------------------------',n)
except:
    pass



