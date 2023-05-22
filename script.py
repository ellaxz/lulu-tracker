import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv()

url = os.environ.get('URL')
color_xpath = os.environ.get('COLOR_XPATH')
size_xpath = os.environ.get('SIZE_XPATH')


def send_email():
    from_addr = os.environ.get('FROM_ADDR')
    to_addr = os.environ.get('TO_ADDR')
    password = os.environ.get('PASSWORD')

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = "Your item is back in stock!"
    body = f"Check out {url}, your item is back in stock!"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

def check_availability():
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    driver.delete_all_cookies()

    driver.get(url)

    # click on the color option
    color = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.XPATH, color_xpath))
)
    color.click()
    print('clicked')
    time.sleep(3)

    try:
        # look for the specific size in the page
        elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, size_xpath))
    )
        print(len(elements))
        # if the size is available, it would return only one element, thus sending the email
        if len(elements) == 1:
            send_email()
    except:
        pass

    driver.quit()
    print('quitttt')


if __name__ == "__main__":
    while True:
        check_availability()
        print('waitttt')
        time.sleep(1800)