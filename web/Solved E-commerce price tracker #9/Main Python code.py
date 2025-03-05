from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import time

# Set up your Edge WebDriver path
webdriver_path = r"N:\Compressed\edgedriver_win64\msedgedriver.exe"

# Define sources
amazon_url = "hhttps://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX1W1XY"
flipkart_url = "https://www.apple.com/in/shop/buy-iphone/iphone-15/6.1%22-display-128gb-black"
croma_url = "https://www.flipkart.com/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4"

# Configure Edge WebDriver options
options = Options()
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--start-maximized')

# Set up Edge WebDriver using the Service class
service = Service(webdriver_path)
wd = webdriver.Edge(service=service, options=options)

print("\n***************************************************************************")
print("                     Starting Program, Please wait ..... \n")

# Flipkart Price Retrieval
print("Connecting to Flipkart...")
wd.get(flipkart_url)
wd.implicitly_wait(10)

try:
    f_price = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]").text
    pr_name = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[1]/h1/span").text
    print(" ---> Successfully retrieved the price from Flipkart \n")
except Exception as e:
    f_price = "Not Found"
    pr_name = "Product Name Not Found"
    print(" ---> Error retrieving price from Flipkart:", e)

time.sleep(2)

# Amazon Price Retrieval
print("Connecting to Amazon...")
wd.get(amazon_url)
wd.implicitly_wait(10)

try:
    a_price = wd.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[4]/div[10]/div[12]/div/table/tbody/tr[2]/td[2]/span[1]").text
    print(" ---> Successfully retrieved the price from Amazon \n")
except Exception as e:
    a_price = "Not Found"
    print(" ---> Error retrieving price from Amazon:", e)

time.sleep(2)

# Croma Price Retrieval
print("Connecting to Croma...")
wd.get(croma_url)
wd.implicitly_wait(10)

try:
    c_price = wd.find_element(By.XPATH, "/html/body/main/div[5]/div[1]/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/div[1]/div/div/span").text
    print(" ---> Successfully retrieved the price from Croma\n")
except Exception as e:
    c_price = "Not Found"
    print(" ---> Error retrieving price from Croma:", e)

time.sleep(2)

# Final display
print("#------------------------------------------------------------------------#")
print(f"Price for [{pr_name}] on all websites, Prices are in INR\n")
print(f"Price available at Flipkart: {f_price}")
print(f"  Price available at Amazon: {a_price}")
print(f"   Price available at Croma: {c_price}")

# Close the browser
wd.quit()
