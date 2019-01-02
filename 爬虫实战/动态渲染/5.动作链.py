from selenium import webdriver
from selenium.webdriver import ActionChains

browers = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browers.get(url)
browers.switch_to.frame('iframeResult')
source = browers.find_elements_by_css_selector('#draggable')
target = browers.find_elements_by_css_selector('#droppable')
actions = ActionChains(browers)
actions.drag_and_drop(source,target)
actions.perform()
