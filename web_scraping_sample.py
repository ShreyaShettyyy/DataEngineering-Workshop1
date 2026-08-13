import requests
from bs4 import BeautifulSoup

url = "https://blog.python.org/blog/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

posts = soup.find_all("article")

for post in posts:
    title = post.find("h3").get_text(strip=True)
    link = post.find("a", href=True)

    print("Title:", title)
    print("URL:", link.get("href"))
    print("-" * 50)