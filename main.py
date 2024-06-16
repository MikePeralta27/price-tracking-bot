from bs4 import BeautifulSoup
import requests
from pprint import pprint
import lxml
import smtplib

URL = "https://www.amazon.com/ASUS-Strix-Gaming-Laptop-Nebula/dp/B0CRD84TFV/ref=sr_1_3?crid=1YRRXG4FWCH&dib=eyJ2IjoiMSJ9.x4XDZEypWbj1D1l1_L27s44tZ1IynaDQJUmX3IBdPs2BKzCi1uQP2bDiNohHXwDw_3wD4EBcsTqi--r3WIti4nodsD5OsgAs4Cern-YjjDgPFSUJu8T_BqjbkICWAQvLBLsy0LTuOn-RtbCov6NPx6xjvuiLrykvIroVJ8eOXNkg6U1SnP8_gaNcaJ8SGTMISTJwDW2-nHskmDPO3IIoorR3gLJlu1gNBP7IcGwNwrySqxE00vDFwS8oNevSHa1f05fWoZgXd0wVjowHlhTkcmLI5Hm9KzIu-H2MG4vCCsw.nps5B3PQm9NdHonTj8BCoODR5bGcUFFXtUIjnCrPej8&dib_tag=se&keywords=ASUS%2BROG%2BStrix%2BScar&qid=1718563398&s=electronics&sprefix=asus%2Brog%2Bstrix%2Bscar%2Celectronics%2C181&sr=1-3&ufe=app_do%3Aamzn1.fos.17f26c18-b61b-4ce9-8a28-de351f41cffb&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,es;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-ch-ua": 'Not/A)Brand";v="8", "Chromium";v="126'
}
MY_EMAIL = "peraltagbh@gmail.com"
MY_PASSWORD = "bowfnpqfabsqsqno"
STANDARD_PRICE = 2849.00
MINIMUM_PRICE = 2849.00
response = requests.get(url=URL, headers=headers)
# pprint(response.content)

soup = BeautifulSoup(response.content, "lxml")
price = soup.find(class_="a-offscreen").get_text()
title = soup.find(id="productTitle").get_text().strip()
price_without_currency = price.split("$")[1]

prince_as_float = float(price_without_currency.replace(',',''))

if prince_as_float <= MINIMUM_PRICE:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="peraltamichaelm27@gmail.com",
                        msg=f"Subject:Amazon Price Alert!\n\n{title} is now ${prince_as_float}\n\n{URL}".encode('utf-8'))
    connection.close()




