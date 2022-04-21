# selenium 大多数情况下用在自动化调式web浏览器

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# option = webdriver.ChromeOptions()
# driver = webdriver.Chrome()
# option.binary_location=r''

browser = webdriver.Chrome(executable_path="D:\JetBrains\Python3.7.3\chromedriver.exe")

browser.get("https://www.baidu.com")

# 调用到搜索框
input = browser.find_element_by_id("kw")

# 传入参数 传输值
input.send_keys("淘宝")

# 电脑调用键盘操作
input.send_keys(Keys.ENTER)

# 导包 设置延时时间
wait = WebDriverWait(browser,10)

# 两个括号的原因是因为调用了两个库里的包
wait.until(EC.presence_of_all_elements_located((By.ID,"content_left")))

# 网址目录
print(browser.current_url)
# 缓存机制
print(browser.get_cookies())