from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://uchi.ru/')

# Авторизация
login = browser.find_element_by_css_selector('#login')
password = browser.find_element_by_css_selector('#password')
submit = browser.find_element_by_css_selector('input[name="commit"]')
WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="commit"]')))

login.send_keys('123')
password.send_keys('топот12744')
submit.click()
