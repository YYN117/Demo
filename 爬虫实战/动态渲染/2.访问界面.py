from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('mq')
input_second = browser.find_element_by_css_selector('#mq')
input_third = browser.find_element_by_xpath('//*[@id="mq"]')
print(input_first,input_second,input_third,end='\n')
browser.close()