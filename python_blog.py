import requests
from bs4 import BeautifulSoup

url = "https://blog.python.org/blog/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

posts = soup.find_all("article")

for post in posts:
    title = post.find("h3").get_text(strip=True)

    text = post.get_text(" ", strip=True)

    # Remove title
    text = text.replace(title, "", 1).strip()

    # The author and date come before the description
    parts = text.split(" · ", 1)

    if len(parts) == 2:
        author = parts[0].strip()

        # Date is the first 3 words after the author
        date = " ".join(parts[1].split()[:3])

        print("Title:", title)
        print("Author:", author)
        print("Date:", date)
        print("-" * 50)