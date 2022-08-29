#Author: yavuz.sh
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
firefox_Options = Options()
firefox_Options.add_argument("--headless")
firefox_Options.add_argument("--window-size=%s" % "1,1")
driver = webdriver.Firefox(options=firefox_Options)
driver.minimize_window()
try:
    driver.get("https://my.nextdns.io/login")
except:
    print("Check your internet connection.")
    exit()
print("Connection is being established...")
time.sleep(1)
userName = input("NextDNS E-Mail: ")
userPass = input("NexDNS Password: ")
userBox = driver.find_element("xpath",'/html/body/div[1]/div/div/div/div[2]/div/form/div[1]/input')
userBox.send_keys(userName)
passBox = driver.find_element("xpath",'/html/body/div[1]/div/div/div/div[2]/div/form/div[2]/input')
passBox.send_keys(userPass)
loginBtn = driver.find_element("xpath",'/html/body/div[1]/div/div/div/div[2]/div/form/button')
loginBtn.click()
time.sleep(4)
try:
    blacklist = driver.find_element("xpath",'/html/body/div[1]/div[1]/div/div/div/div[2]/div[5]/a')
    blacklist.click()
except:
    print("Check your e-mail or password.")
    exit()    
time.sleep(1)
newDomainBox = driver.find_element("xpath", '/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div/input')

listDeny = open('denylist.txt', 'r')
domains = listDeny.readlines()
count = 0
for domain in domains:
    newDomainBox.clear()
    newDomainBox.clear()
    time.sleep(0.3)
    newDomainBox.send_keys(domain)
    time.sleep(0.3)
    newDomainBox.send_keys(Keys.ENTER)
    newDomainBox.send_keys(Keys.ENTER)
    time.sleep(0.3)
    newDomainBox.clear()
    newDomainBox.clear()
    count += 1
    if count % 10 == 0:
        time.sleep(20)     
print("Added domains: " + str(count))

