import lxml
import requests
import smtplib
from bs4 import BeautifulSoup

BUY_PRICE = 200
my_email = your_email
password = your_password
product_URL = "https://www.amazon.com/Alpinestars-Mens-Motorbike-Motorcycle-Black/dp/B07V4NVF2X/ref=sr_1_8?crid=31HJQVH955DS1&keywords=motorbike&qid=1648802698&sprefix=motorbik%2Caps%2C310&sr=8-8"

response = requests.get(product_URL, headers={"Accept-Language":"en-us","User-Agent":"your_text"})
product_html = response.text

soup = BeautifulSoup(product_html, "lxml")

product_price_html = soup.find(name="span", class_="a-offscreen")
product_price_text = product_price_html.getText()
product_price = product_price_text.split('$')[1]
product_price = float(product_price)
print(product_price)

product_title = soup.find(id="title_feature_div").getText().strip()
print(product_title)


if product_price < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Amazon Price Alert!\n\n{product_title} is now ${product_price_text}\n{product_URL}"
                            )


