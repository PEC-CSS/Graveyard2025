from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def fetch_page_source(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    service = Service(r"N:\Compressed\chrome-win64\chrome-win64\chrome.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    time.sleep(5)
    page_source = driver.page_source
    driver.quit()
    return page_source

def extract_price(page_source, tag, class_name):
    soup = BeautifulSoup(page_source, "html.parser")
    element = soup.find(tag, class_=class_name)
    return element.get_text(strip=True) if element else "0"

def clean_price(price):
    return int(price.replace(",", "").replace("₹", "").replace("Rs. ", "").replace("INR", "").split('.')[0])

def get_best_price(product):
    products = {
        "1": {
            "name": "Casio Fx 82MS Calculator",
            "mrp": 625,
            "urls": {
                "Amazon": "https://www.amazon.in/Casio-Non-Programmable-Scientific-Calculator-Functions/dp/B00AXHBBXU",
                "ToppersKit": "https://topperskit.com/products/casio-fx-82ms-2nd-gen-non-programmable-scientific-calculator-pack-of-1",
                "Instamart": "https://www.swiggy.com/stores/instamart/p/casio-fx-82ms-2nd-gen-calculator-black"
            },
            "selectors": {
                "Amazon": ("span", "a-price-whole"),
                "ToppersKit": ("span", "price-item price-item--regular"),
                "Instamart": ("div", "sc-gEvEer iQcBUp _2XPBo")
            }
        },
        "2": {
            "name": "Advanced Engineering Mathematics 10E",
            "mrp": 1199,
            "urls": {
                "Amazon": "https://www.amazon.in/Kreyszig-Advanced-Engineering-Mathematics-International/dp/B0CKNJF9HX",
                "Atlantic Books": "https://atlanticbooks.com/products/advanced-engineering-mathematics-10ed-isv-9788126554232",
                "Wiley India": "https://www.wileyindia.com/advanced-engineering-mathematics-10ed-isv.html"
            },
            "selectors": {
                "Amazon": ("span", "a-price-whole"),
                "Atlantic Books": ("span", "money"),
                "Wiley India": ("p", "pr-price")
            }
        },
        "3": {
            "name": "Whoop 4.0",
            "mrp": 45000,
            "urls": {
                "Amazon": "https://www.amazon.in/Whoop-4.0-Subscription-Wearable-Activity/dp/B0D83WCMBY",
                "Flipkart": "https://www.flipkart.com/whoop-4-0-12-month-subscription-wearable-health-fitness-activity-tracker-smartwatch/p/itm85144628074bc",
                "Hustle Culture": "https://hustleculture.co.in/products/whoop-4-0-storm-grey-hydroknit-band"
            },
            "selectors": {
                "Amazon": ("span", "a-price-whole"),
                "Flipkart": ("div", "Nx9bqj CxhGGd yKS4la"),
                "Hustle Culture": ("span", "price-item price-item--regular")
            }
        },
        "4": {
            "name": "Fireboltt Brillia",
            "mrp": 18999,
            "urls": {
                "Amazon": "https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX1W1XY",
                "Flipkart": "https://www.apple.com/in/shop/buy-iphone/iphone-15/6.1%22-display-128gb-black",
                "Fireboltt": "https://www.flipkart.com/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4"
            },
            "selectors": {
                "Amazon": ("span", "a-price-whole"),
                "Flipkart": ("div", "Nx9bqj CxhGGd"),
                "Fireboltt": ("span", "money")
            }
        }
    }
    
    if product not in products:
        print("Invalid selection.")
        return
    
    data = products[product]
    prices = {}
    
    for site, url in data["urls"].items():
        page_source = fetch_page_source(url)
        tag, class_name = data["selectors"].get(site, (None, None))
        prices[site] = clean_price(extract_price(page_source, tag, class_name))
    
    max_p = min(prices, key=prices.get)
    d, p = round(((data["mrp"] - prices[max_p]) / data["mrp"]) * 100, 2), prices[max_p]
    print(f"Product: {data['name']} (MRP=₹{data['mrp']})\n\nThe website offering the maximum discount is {max_p} with a discount of {d}%.\nPrice: ₹{p}\nURL: {data['urls'][max_p]}\nTo follow link press Ctrl and then click")

print("Select a product:")
print("1: Casio Fx 82MS Calculator - ₹625")
print("2: Advanced Engineering Mathematics 10E - ₹1199")
print("3: Whoop 4.0 - ₹45000")
print("4: Fireboltt Brillia - ₹18999")

choice = input("Enter the number of the product you want to check: ")
get_best_price(choice)
