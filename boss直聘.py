from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
driver = webdriver.Chrome(r'./chromedriver')
# 用get打开百度页面
driver.get("https://account.iiyi.com/")
#driver.find_elements_by_xpath('//*[@id="main"]/div/div[2]/ul/li[1]/div/div[1]/div[1]/div/div[1]/span[1]/a').click()
#driver.find_elements_by_xpath('//*[@id="main"]/div/div[2]/ul/li[1]/div/div[1]/div[1]/div/div[1]/span[1]/a')


#driver.find_element_by_name('query').send_keys('python')
#点击搜索按钮
driver.find_element_by_id('userinfo').send_keys('15150661019')
driver.find_element_by_id('password').send_keys('zh123456')
driver.find_element_by_class_name('submit').click()

# bro.find_element_by_id('username').send_keys('www.zhangbowudi@qq.com')
# time.sleep(2)
# bro.find_element_by_id('password').send_keys('bobo_15027900535')
# time.sleep(2)
# bro.find_element_by_id('loginSub').click()
# time.sleep(30)
# bro.quit()