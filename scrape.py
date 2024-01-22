
import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import time
import schedule

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def find_price():
    # url = "https://www.flipkart.com/philips-bt3101-15-trimmer-45-min-runtime-10-length-settings/p/itm4b45b688873c9?pid=TMRFSEJ5WSW82ZDN&cmpid=product.share.pp&_refId=PP.773ae55f-b5ac-4c48-ac17-b13db141651f.TMRFSEJ5WSW82ZDN&_appId=CL"
    url = "https://amzn.eu/d/6sd5Wfo"
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    start_time = time.time()

    response = requests.get(url, verify=False)
    end_time = time.time()
    print("find_price")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price_str = soup.find('span', {'class': 'a-offscreen'}).string[1:]
        # print(price_str)
        price = float(price_str.replace(',', ''))

        if int(price) <= 3100:
            # print(price)
            send_email(price)
        # else:
            # print()
            # print(price)
    # print(price)
    # print(response.status_code)

def send_email(price):
    sender_email = "snehith1233@gmail.com"
    sender_password = "klyr uzob ckhk fuen"
    receiver_email = "snehith1233@gmail.com"
# <span id="tp_price_block_total_price_ww" class="a-price" data-a-size="m" data-a-color="price"><span class="a-offscreen">₹3,499.00</span><span aria-hidden="true"><span class="a-price-symbol"></span><span class="a-price-whole">3,499<span class="a-price-decimal">.</span></span><span class="a-price-fraction">00</span></span></span>
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Price Alert: jbl earbuds"

    text_part = MIMEText("https://amzn.eu/d/6sd5Wfo")
    message.attach(text_part)

    body = f"The price of jbl earphones has reduced  {price}. Check it now!"
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

schedule.every(30).minutes.do(find_price)

while True:
    print("in the function")
    schedule.run_pending()
    time.sleep(1780)
