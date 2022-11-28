# Buy a MacBook on Amazon when the script is run
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# go to the amazon home page
driver.get("http://www.amazon.com")

# the page is ajaxy so the title is originally this:
print(driver.title)

# find the element that's name attribute is q (the amazon search box)
inputElement = driver.find_element_by_name("field-keywords")

# type in the search
inputElement.send_keys("MacBook")

# submit the form (although google automatically searches now without submitting)
inputElement.submit()

# wait for the search results to load
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "s-result-count")))
    print(driver.title)
except:
    print("Search results did not load")

# click on the first result
driver.find_element_by_xpath("//*[@id='result_0']/div/div/div/div[2]/div[1]/div[1]/a/h2").click()

# wait for the product page to load
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "add-to-cart-button")))
    print(driver.title)
except:
    print("Product page did not load")

# click on the add to cart button
driver.find_element_by_id("add-to-cart-button").click()

# wait for the cart page to load
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "hlb-ptc-btn-native")))
    print(driver.title)
except:
    print("Cart page did not load")

# click on the proceed to checkout button
driver.find_element_by_id("hlb-ptc-btn-native").click()

# wait for the sign in page to load
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ap_email")))
    print(driver.title)
except:
    print("Sign in page did not load")

# type in the email
driver.find_element_by_id("ap_email").send_keys("email@email.com")

# type in the password
driver.find_element_by_id("ap_password").send_keys("password")

# click on the sign in button
driver.find_element_by_id("signInSubmit").click()

# wait for the delivery page to load
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "address-book-entry-0")))
    print(driver.title)
except:
    print("Delivery page did not load")

# click on the delivery address
driver.find_element_by_id("address-book-entry-0").click()

# wait for the payment page to load
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pm_0")))
    print(driver.title)
except:
    print("Payment page did not load")

# click on the payment method
driver.find_element_by_id("pm_0").click()

# wait for the place your order page to load
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "placeYourOrder1")))
    print(driver.title)
except:
    print("Place your order page did not load")

# click on the place your order button
driver.find_element_by_id("placeYourOrder1").click()

# wait for the order confirmation page to load
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "order-number")))
    print(driver.title)
except:
    print("Order confirmation page did not load")

# print the order number
print(driver.find_element_by_id("order-number").text)

# close the browser
driver.close()
