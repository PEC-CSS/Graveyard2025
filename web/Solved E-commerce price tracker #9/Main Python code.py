from bs4 import BeautifulSoup

def extract_price(file, tag, class_name=None, data_attr=None):
    with open(file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        element = soup.find(tag, attrs={data_attr: True}) if data_attr else soup.find(tag, class_=class_name)
        return element[data_attr] if data_attr and element else element.get_text(strip=True) if element else "0"

def clean_price(price):
    return int(price.replace(",", "").replace("₹", "").split('.')[0])

def get_prices():    
    amazon = r"C:\Users\Naman Vasudev\Desktop\New folder\Amazon.html"
    flipkart = r"C:\Users\Naman Vasudev\Desktop\New folder\Flipkart.html"
    vijaysales = r"C:\Users\Naman Vasudev\Desktop\New folder\Vijay Sales.html"
    firebolt = r"C:\Users\Naman Vasudev\Desktop\New folder\Firebolt.html"
    
    urls = {
        "Amazon": "https://www.amazon.in/Fire-Boltt-BSW215-Brillia-Dark-Grey/dp/B0D2KGBVX4?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&smid=ACP3LRBIG2716&th=1",
        "Flipkart": "https://www.flipkart.com/fire-boltt-brillia-51-3mm-2-02-inch-largest-amoled-display-bluetooth-calling-ai-assistant-smartwatch/p/itm306790dfedcd4?pid=SMWHFHUHJZACXUTZ&lid=LSTSMWHFHUHJZACXUTZJ5FXST&marketplace=FLIPKART",
        "Vijay Sales": "https://www.vijaysales.com/p/231206/fire-boltt-brillia-smart-watch-with-2-02-inch-amoled-display-bluetooth-calling-ip67-dust-water-resistant-120-plus-sports-modes-silver",
        "Firebolt": "https://www.fireboltt.com/products/brillia"
    }
    prices = {
        "Amazon": clean_price(extract_price(amazon, "span", class_name="a-price-whole")),
        "Flipkart": clean_price(extract_price(flipkart, "div", class_name="Nx9bqj CxhGGd")),
        "Vijay Sales": clean_price(extract_price(vijaysales, "span", data_attr="data-final-price")),
        "Firebolt": clean_price(extract_price(firebolt, "span", class_name="money"))
    }
    m, max_p = 18999, min(prices, key=prices.get)
    d, p = round(((m - prices[max_p]) / m) * 100, 2), prices[max_p]
    print(f"Product: Fireboltt Brillia (MRP=₹{m})\n\nThe website offering the maximum discount is {max_p} with a discount of {d}%.\nPrice: ₹{p}\nURL: {urls[max_p]}\nTo follow link press Ctrl and then click")

get_prices()