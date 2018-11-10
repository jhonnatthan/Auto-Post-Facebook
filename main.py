import time
import csv
import codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--mute-audio")
# options.add_argument("headless")
driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
driver.get('https://mbasic.facebook.com/login/')
driver.maximize_window()
wait = WebDriverWait(driver, 10)
print("Opened facebook...")
file = codecs.open('post.txt', encoding='utf-8', mode='r')

with open('users.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        email = driver.find_element_by_xpath("//*[@id='m_login_email']")
        email.clear()
        email.send_keys(row[0])
        print("email entered...")
        password = driver.find_element_by_xpath("//*[@id='login_form']/ul/li[2]/div/input")
        password.clear()
        password.send_keys(row[1])
        print("Password entered...")
        time.sleep(2)
        button = driver.find_element_by_xpath("//*[@id='login_form']/ul/li[3]/input")
        button.click()
        print("facebook opened")
        time.sleep(2)
        touchbutton = driver.find_element_by_xpath("//*[@id='root']/table/tbody/tr/td/div/div[3]/a")
        touchbutton.click()
        time.sleep(2)
        print("Entrar com um toque")
        status = driver.find_element_by_xpath("//*[@id='mbasic_inline_feed_composer']/form/table/tbody/tr/td[2]/div/textarea")
        driver.execute_script('arguments[0].value = arguments[1]', status, file.read())
        # status.send_keys(file.read())
        print("Status trying")
        postbutton = driver.find_element_by_xpath('//*[@id="mbasic_inline_feed_composer"]/form/table/tbody/tr/td[3]/div/input')
        postbutton.click()
        time.sleep(2)
        print("post done")
        menubutton = driver.find_element_by_xpath('//*[@id="header"]/div/a[8]')
        menubutton.click()
        time.sleep(2)
        logoutbutton = driver.find_element_by_xpath('//*[@id="mbasic_logout_button"]')
        logoutbutton.click()
        driver.get('https://mbasic.facebook.com/login/?ref=dbl&fl&refid=8')
        wait.until(EC.url_changes('https://mbasic.facebook.com/login/?ref=dbl&fl&refid=8'))
    driver.close()
