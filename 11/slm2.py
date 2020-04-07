from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# 交互操作
# 将动作附加到 动作链中串行执行

# 实现浏览器自动调用
browser = webdriver.Chrome()

# 获取网址
url = "https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"

# 将网址给自动运行
browser.get(url)

#获取蒙版id
browser.switch_to.frame("iframeResult")

#获取到两个面板的id并用css选择器调用
tuodong = browser.find_element_by_css_selector("#dropable")
anpai = browser.find_element_by_css_selector("#dropable")

# 如何移动
actions = ActionChains(browser)

# dtag_and_drop是一个行为方法
actions.drag_and_drop(tuodong,anpai)

# 适应距离
actions.perform()