from bs4 import BeautifulSoup
import requests

url = "https://www.tutorialspoint.com/index.htm"
req = requests.get(url)

htmlcontant = req.content
# print(htmlcontant)

# mainly 3 objects
# 1. Tag
# 2. NavigableString
# 3. BeutifulSoup
# 4. comment


# title
soup = BeautifulSoup(htmlcontant, "html.parser")
print(soup.prettify)

