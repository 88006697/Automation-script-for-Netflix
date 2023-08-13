from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Credentials import LoginID, password

driver = webdriver.Chrome()
driver.get('https://netflix.com')
time.sleep(2)

# try the close cookie button to see if it works properly
try:
    cookie = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/button').click()
except:
    print("Couldn't locate the 'close cookie' button.")
time.sleep(2)


# try if the get started part works
try:
    getStartedEmail = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/form/div/div/div/input')
    getStartedEmail.send_keys(LoginID)
except:
    print("Couldn't enter the email for Get Started.")
time.sleep(2)
try:
    getStarted = driver.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/form/div/button').click()
except:
    print("Couldn't locate the 'Get Started' button.")
time.sleep(2)
# After clicking get started button, check if will lead you to the correct site
get_url = driver.current_url
if str(get_url) != 'https://www.netflix.com/signup/password?locale=en-CA':
    print ("The Get Started link doesn't direct to the correct site")
# Check after clicking the Netflix Homepage, will it lead to the correct site
try:
    homePage = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/a[1]').click()
except:
    print("Couldn't locate the 'Netflix Home' button.")
time.sleep(2)
get_url = driver.current_url
if str(get_url) != 'https://www.netflix.com/ca/':
    print ("The Netflix Home link doesn't direct to the correct site")
# Check after clicking the Netflix Homepage, will it lead to the correct site

# try the "Frequently Asked Questions" to see if they can be clicked and the following content will pop up
driver.execute_script('window.scrollBy(0, 2500)') 
time.sleep(2)
try:
    question1 = driver.find_element(By.XPATH, '//*[@id="button--nmhp-card-faq-accordion--0"]').click()
except:
    print("Couldn't locate the 'What is netflix' button.")
try:
    outQuestion1 = driver.find_element(By.XPATH, '//*[@id="content--nmhp-card-faq-accordion--0"]')
except:
    print("Couldn't locate the output after clicking 'What is netflix' button.")
time.sleep(2)

try:
    question2 = driver.find_element(By.XPATH, '//*[@id="button--nmhp-card-faq-accordion--1"]').click()
except:
    print("Couldn't locate the 'How much does Neflix cost' button.")
try:
    outQuestion2 = driver.find_element(By.XPATH, '//*[@id="content--nmhp-card-faq-accordion--1"]/span')
except:
    print("Couldn't locate the output after clicking 'How much does Neflix cost' button.")
time.sleep(2)


# try the FAQ link at the bottom of the page to see if they work
driver.execute_script('window.scrollBy(0, 4000)') 
time.sleep(2)
try:
    FAQ = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/footer/div/div[2]/div/ul/li[1]/a').click()
except:
    print("Couldn't locate the 'FAQ' link button.")
# Check if the link direct to the correct website
get_url = driver.current_url
if str(get_url) != 'https://help.netflix.com/en/node/412':
    print ("The FAQ link doesn't direct to the correct site")
time.sleep(2)

# try if the Netflix homepage button works
try:
    FAQ = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]').click()
except:
    print("Couldn't locate the 'Netflix Homepage' link button.")
time.sleep(2)
get_url = driver.current_url
if str(get_url) != 'https://www.netflix.com/ca/':
    print ("The Netflix Homepage link doesn't direct to the correct site")
time.sleep(2)

# try the Help center link at the bottom of the page to see if they work
driver.execute_script('window.scrollBy(0, 4000)') 
time.sleep(2)
try:
    helpCenter = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/footer/div/div[2]/div/ul/li[2]/a').click()
except:
    print("Couldn't locate the 'Help center' link button.")
# Check if the link direct to the correct website
get_url = driver.current_url
if str(get_url) != 'https://help.netflix.com/en/':
    print ("The FAQ link doesn't direct to the correct site")
time.sleep(2)

# try if the Netflix homepage button works
try:
    FAQ = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]').click()
except:
    print("Couldn't locate the 'Netflix Homepage' link button.")
time.sleep(2)
get_url = driver.current_url
if str(get_url) != 'https://www.netflix.com/ca/':
    print ("The Netflix Homepage link doesn't direct to the correct site")
time.sleep(2)

# try the Sign in button to see if it works properly
try:
    signIn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/header/div/span[3]/a').click()
except:
    print("Couldn't locate the 'Sign in' button.")
time.sleep(2)

# try to enter the username to see if it works properly
try:
    emailId = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input')
except:
    print("Couldn't enter the username.")
time.sleep(2)

# try to enter the password to see if it works properly
try:
    emailPassword = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div[1]/div/label/input')
    emailPassword.send_keys(password)
except:
    print("Couldn't enter the password.")
time.sleep(2)

# try the login button to see if it works properly
try:
    logInButton = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[1]/form/button').click()
except:
    print("Couldn't locate the 'login' button.")
time.sleep(5)

