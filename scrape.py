
import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import time
import schedule

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def find_price():
    url = "https://www.flipkart.com/philips-bt3101-15-trimmer-45-min-runtime-10-length-settings/p/itm4b45b688873c9?pid=TMRFSEJ5WSW82ZDN&cmpid=product.share.pp&_refId=PP.773ae55f-b5ac-4c48-ac17-b13db141651f.TMRFSEJ5WSW82ZDN&_appId=CL"
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    start_time = time.time()

    response = requests.get(url, verify=False)
    end_time = time.time()

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price_str = soup.find('div', {'class': '_30jeq3 _16Jk6d'}).string[1:]
        price = float(price_str.replace(',', ''))

        if price <= 1200:
            send_email(price)
        else:
            print(price)
def send_email(price):
    sender_email = "snehith1233@gmail.com"
    sender_password = "lnfo jigu iooi oqka"
    receiver_email = "snehith1233@gmail.com"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Price Alert: Philips Trimmer"

    text_part = MIMEText("https://www.flipkart.com/philips-bt3101-15-trimmer-45-min-runtime-10-length-settings/p/itm4b45b688873c9?pid=TMRFSEJ5WSW82ZDN&cmpid=product.share.pp&_refId=PP.773ae55f-b5ac-4c48-ac17-b13db141651f.TMRFSEJ5WSW82ZDN&_appId=CL")
    message.attach(text_part)

    body = f"The price of the Philips Trimmer has dropped to {price}. Check it now!"
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

schedule.every(10).seconds.do(find_price)

while True:
    schedule.run_pending()
    time.sleep(10)
