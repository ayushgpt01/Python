from selenium import webdriver
from selenium.webdriver import ActionChains

chrome_browser = webdriver.Chrome('./chromedriver.exe')
chrome_browser.maximize_window()
chrome_browser.get('https://testautomationpractice.blogspot.com/')
action = ActionChains(chrome_browser)

input = chrome_browser.find_element_by_id('field1')
input.clear()
input.send_keys('Wow copied??')
btn = chrome_browser.find_elements_by_tag_name('button')
action.double_click(btn)