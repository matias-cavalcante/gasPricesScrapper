
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

# Browsing options
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')


url = 'https://www.n1.is/thjonusta/eldsneyti/daeluverd/'

#driver = webdriver.Chrome()
driver = webdriver.Chrome(options=options)
driver.get(url)


def stationLocationName(data):
    unfilteredName = data.find_element(By.TAG_NAME, "h4")
    toFilterName = unfilteredName.text.split(" ")
    if len(toFilterName) == 1:
        return toFilterName[0]
    elif len(toFilterName) == 2:
        return toFilterName[1]
    else:
        return toFilterName[2]


def flawedPrice(price):
    if price == '0':
        return int(price)
    elif len(price) == 0:
        return "failed"


def fuelTypeValueFinder(data, fuel):
    fuelResults = data.find_element_by_xpath(
        './/span[text()="{}"]'.format(fuel))
    fuelPrice = fuelResults.find_element_by_xpath('following-sibling::div')
    fuelPrice = fuelPrice.text
    if flawedPrice(fuelPrice) == 0 or flawedPrice(fuelPrice):
        return fuelPrice
    fuelPriceConverted = float(fuelPrice.replace(",", "."))
    return fuelPriceConverted


def clickAndFetch():
    jsonN1 = {}
    bensin = '.css-1635yco.epw6mxe6'
    buttons = driver.find_elements(By.CSS_SELECTOR, '.css-1ssumb9.eoreqqy2')
    regionsSection = driver.find_elements(
        By.CSS_SELECTOR, '.css-1nwxvlr.eoreqqy0')
    regionsJumper = 0

    for btn in buttons:
        WebDriverWait(driver, 6).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.css-1ssumb9.eoreqqy2')))
        btn.click()
        time.sleep(2)

        sectionData = regionsSection[regionsJumper].find_elements(
            By.CSS_SELECTOR, '.css-pdy5sh.epw6mxe0')

        for block in sectionData:
            stationName = stationLocationName(block)
            bensinPrice = fuelTypeValueFinder(block, 'Bensín')
            diselPrice = fuelTypeValueFinder(block, 'Dísel')
            jsonN1[stationName] = {bensinPrice, diselPrice}
        regionsJumper = regionsJumper + 1
    return jsonN1


#n1PricesToData = clickAndFetch()


# for key, value in n1PricesToData.items():
#    print(f'{key}: {value}')
