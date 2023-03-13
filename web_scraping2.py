#importing modules
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=options)
source =driver.get('https://analyticsindiamag.com/')
source_code=driver.page_source

soup = BeautifulSoup(source_code,'lxml')
article_block =soup.find_all('div',class_='post-title')

for titles in article_block:
	title =titles.find('span').get_text()
	print(title)
