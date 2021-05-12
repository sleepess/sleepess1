from selenium import webdriver
import time
chromedriver = webdriver.Chrome()
chromedriver.get("C:\pythonzidonghuatest\自动化\day1\day01\资料\练习的html\练习的html\跳转页面\pop.html")
chromedriver.maximize_window()
chromedriver.find_element_by_xpath("//*[@id='goo']").click()
chromedriver.switch_to.window(chromedriver.window_handles[1])#选择标签（点击标签后，页面跳转，程序没有跳转，需要让程序进行界面跳转）
chromedriver.find_element_by_id("kw").send_keys("java")
chromedriver.find_element_by_id("su").click()
time.sleep(3)
chromedriver.quit()
