# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import re
from pyquery import PyQuery as pq
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)

def search():
    try:
        browser.get('https://www.jd.com')
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#key")))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#search > div > div.form > button")))
        input.send_keys('Python')
        submit.click()
        # browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        sleep(1)
        js = 'document.documentElement.scrollTop=10000'
        browser.execute_script(js)
        sleep(1)
        # browser.execute_script("document.body.scrollTop=1000")
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#J_bottomPage > span.p-skip > em:nth-child(1) > b")))
        get_products()
        return total.text
    except TimeoutException:
        return search()

def next_page(page_number):
    try:
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#J_bottomPage > span.p-skip > input")))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_bottomPage > span.p-skip > a")))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#J_bottomPage > span.p-num > a.curr"),str(page_number)))
        sleep(1)
        js = 'document.documentElement.scrollTop=10000'
        browser.execute_script(js)
        sleep(1)
        get_products()
    except TimeoutException:
        next_page(page_number)

def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#J_goodsList .gl-warp .gl-item")))
    html = browser.page_source
    doc = pq(html)
    items = doc("#J_goodsList .gl-warp .gl-item").items()
    # print(items)
    file = open('python.txt', 'a', encoding='utf-8')
    for item in items:
        products = {
            'image':item.find('.p-img a img').attr('src'),
            'price':item.find('.p-price').text()[2:],
            'deal':item.find('.p-commit').text().replace('\n',''),
            'title':item.find('.p-name').text().replace('\n',''),
            'shop':item.find('.p-shopnum').text(),
        }
        print(products)
        file.write('图片：' + products[0] + '\n' + '价格：' + products[1] + '\n' + '销量：' + products[2])
    file.close()

def main():
    total = search()
    # total = int(re.compile('(\d+)').search(total).group(1))
    total = int(total)
    # print(total)
    # print(type(total))
    for i in range(2,3):
        next_page(i)


if __name__ == '__main__':
    main()
