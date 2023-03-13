# Import Library
from selenium import webdriver
import pandas as pd

# Open Browser
driver = webdriver.Chrome()
# Get the  URL
url = 'https://www.w3schools.com/html/html_tables.asp'
driver.get(url)
driver.maximize_window()
# Read and Convert Web table into data frame
webtable_df = pd.read_html(driver.find_element_by_xpath("//table[@id='customers']").get_attribute('outerHTML'))[0]
print(webtable_df)
# Write() to CSV file
webtable_df.to_csv('/home/pys/customers.csv')
