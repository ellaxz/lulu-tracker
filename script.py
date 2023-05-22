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
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")


    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=chrome_options)  # Pass chrome_options

    
    # s=Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=s)

    driver.delete_all_cookies()

    driver.get(url)

    # click on the color option
    print('chech')
    try:
        color = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, color_xpath))
        )
        color.click()
        print('clicked')
        time.sleep(3)
    except Exception as e:
        print(e)

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