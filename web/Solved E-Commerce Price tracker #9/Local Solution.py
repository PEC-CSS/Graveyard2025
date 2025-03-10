from bs4 import BeautifulSoup

def extract_price(file, tag, class_name):
    with open(file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        element = soup.find(tag, class_=class_name)
        return element.get_text(strip=True) if element else "0"

def clean_price(price):
    return int(price.replace(",", "").replace("₹", "").replace("Rs. ", "").replace("INR", "").split('.')[0])

def price_before_discount(file, tag, class_name):
    return clean_price(extract_price(file, tag, class_name))

def get_best_price(product):
    products = {
        "1": {
            "name": "Casio Fx 82MS Calculator",
            "files": {
                "Amazon": r"C:\Users\Naman Vasudev\Desktop\Price Tracker\Amazon-C.html",
                "ToppersKit": r"C:\Users\Naman Vasudev\Desktop\Price Tracker\ToppersKitC.html",
                "Instamart": r"C:\Users\Naman Vasudev\Desktop\Price Tracker\Instamart.html"
            },
            "urls": {
                "Amazon": "https://www.amazon.in/Casio-Non-Programmable-Scientific-Calculator-Functions/dp/B00AXHBBXU",
                "ToppersKit": "https://topperskit.com/products/casio-fx-82ms-2nd-gen-non-programmable-scientific-calculator-pack-of-1",
                "Instamart": "https://www.swiggy.com/stores/instamart/p/casio-fx-82ms-2nd-gen-calculator-black"
            },
            "selectors": {
                "Amazon": ("span", "a-price-whole"),
                "ToppersKit": ("span", "price-item price-item--regular"),
                "Instamart": ("div", "sc-gEvEer iQcBUp _2XPBo")
            },
            "mrp_selectors": {             
                "Instamart": ("div", "sc-gEvEer iQcBUp _2XPBo")
            }
        },
        "2": {
            "name": "Advanced Engineering Mathematics 10E",
            "files": {
                "Amazon": r"C:\Users\Naman Vasudev\Desktop\Price Tracker\Amazon Book.html",
                "Atlantic Books": r"C:\Users\Naman Vasudev\Desktop\Price Tracker\Atlantic Book.html",
                "Wiley India": r"C:\Users\Naman Vasudev\Desktop\Price Tracker\Wiley Book.html"
            },
            "urls": {
                "Amazon": "https://www.amazon.in/Kreyszig-Advanced-Engineering-Mathematics-International/dp/B0CKNJF9HX",
                "Atlantic Books": "https://atlanticbooks.com/products/advanced-engineering-mathematics-10ed-isv-9788126554232",
                "Wiley India": "https://www.wileyindia.com/advanced-engineering-mathematics-10ed-isv.html"
            },
            "selectors": {
                "Amazon": ("span", "a-price-whole"),
                "Atlantic Books": ("span", "money"),
                "Wiley India": ("p", "pr-price")
            },
            "mrp_selectors": {
                "Amazon": ("span", "a-offscreen")
            }
        },
        "3": {
            "name": "Whoop 4.0",
            "files": {
                "Amazon": r"C:\Users\Naman Vasudev\Desktop\Price Tracker\Amazon Whoop.html",
                "Flipkart": r"C:\Users\Naman Vasudev\Desktop\Price Tracker\Flipkart Whoop.html",
                "Hustle Culture": r"C:\Users\Naman Vasudev\Desktop\Price Tracker\Hustle Culture Whoop.html"
            },
            "urls": {
                "Amazon": "https://www.amazon.in/Whoop-4.0-Subscription-Wearable-Activity/dp/B0D83WCMBY",
                "Flipkart": "https://www.flipkart.com/whoop-4-0-12-month-subscription-wearable-health-fitness-activity-tracker-smartwatch/p/itm85144628074bc",
                "Hustle Culture": "https://hustleculture.co.in/products/whoop-4-0-storm-grey-hydroknit-band"
            },
            "selectors": {
                "Amazon": ("span", "a-price-whole"),
                "Flipkart": ("div", "Nx9bqj CxhGGd yKS4la"),
                "Hustle Culture": ("span", "price-item price-item--regular")
            },
            "mrp_selectors": {
                "Flipkart": ("div","yRaY8j A6+E6v yKS4la")
            }

        },
        "4": {
            "name": "Fireboltt Brillia",
            "files": {
                "Amazon": r"C:\Users\Naman Vasudev\Desktop\Price Tracker\Amazon.html",
                "Flipkart": r"C:\Users\Naman Vasudev\Desktop\Price Tracker\Flipkart.html",
                "Fireboltt": r"C:\Users\Naman Vasudev\Desktop\Price Tracker\Firebolt.html"
            },
            "urls": {
                "Amazon": "https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX1W1XY",
                "Flipkart": "https://www.apple.com/in/shop/buy-iphone/iphone-15/6.1%22-display-128gb-black",
                "Fireboltt": "https://www.flipkart.com/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4"
            },
            "selectors": {
                "Amazon": ("span", "a-price-whole"),
                "Flipkart": ("div", "Nx9bqj CxhGGd"),
                "Fireboltt": ("span", "money")
            },
            "mrp_selectors": {
                "Amazon": ("span", "a-size-mini a-color-secondary aok-nowrap a-text-strike")
            }
        }
    }
    
    if product not in products:
        print("Invalid selection.")
        return
    
    data = products[product]
    prices = {}
    mrp = 0
    

    for site, file in data["files"].items():
        if site in data["mrp_selectors"]:
            tag, class_name = data["mrp_selectors"][site]
            mrp = price_before_discount(file, tag, class_name)
            if mrp > 0:
                break

    for site, file in data["files"].items():
        tag, class_name = data["selectors"].get(site, (None, None))
        prices[site] = clean_price(extract_price(file, tag, class_name))
    

    max_p = min(prices, key=prices.get)
    discount_percentage = round(((mrp - prices[max_p]) / mrp) * 100, 2)
    best_price = prices[max_p]
    
    print(f"Product: {data['name']} (MRP=₹{mrp})\n")
    print(f"The website offering the maximum discount is {max_p} with a discount of {discount_percentage}%.")
    print(f"Price: ₹{best_price}")
    print(f"URL: {data['urls'][max_p]}")
    print("To follow the link, press Ctrl and then click.")

print("Select a product:")
print("1: Casio Fx 82MS Calculator")
print("2: Advanced Engineering Mathematics 10E")
print("3: Whoop 4.0")
print("4: Fireboltt Brillia")

choice = input("Enter the number of the product you want to check: ")
get_best_price(choice)


