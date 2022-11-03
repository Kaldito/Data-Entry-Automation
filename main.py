import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# -------------------- CONSTANTS -------------------- #
BASE_URL = "https://www.inmuebles24.com"
URL = f"{BASE_URL}/casas-o-departamentos-en-renta-en-torreon.html"
FORMS = "FILL WITH A VALID FORMS URL"

# -------------------- SCRIPT -------------------- #
# - Selenium config
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)

time.sleep(1)

# - List making
prices = []
addresses = []
links = []

# - Information gathering
cards = driver.find_elements(By.CSS_SELECTOR, ".sc-1tt2vbg-3")
for card in cards:
    link_div = card.find_element(By.CSS_SELECTOR, ".sc-i1odl-0")
    link = link_div.get_attribute("data-to-posting")
    price = card.find_element(By.CSS_SELECTOR, ".sc-12dh9kl-4")
    address = card.find_element(By.CSS_SELECTOR, ".sc-i1odl-11")

    links.append(f"{BASE_URL}{link}")
    prices.append(price.text.split()[1].replace(",", ""))
    addresses.append(address.text)

# - Forms responses
for i in range(0, len(links)):
    driver.get(FORMS)

    inputs = driver.find_elements(By.CSS_SELECTOR, ".whsOnd")
    inputs[0].send_keys(addresses[i])
    inputs[1].send_keys(prices[i])
    inputs[2].send_keys(links[i])

    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()

driver.quit()
