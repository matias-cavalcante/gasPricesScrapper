
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


# Browsing options
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')


url = 'https://www.n1.is/thjonusta/eldsneyti/daeluverd/'


driver = webdriver.Chrome()
driver.get(url)


regionsBtns = '.css-1ssumb9.eoreqqy2'
boxes = '.css-pdy5sh.epw6mxe0'


def clickAndFetch(regbuttons, cajas):
    buttons = driver.find_elements(By.CSS_SELECTOR, regbuttons)

    for btn in buttons:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, regbuttons
             )))
        btn.click()
        time.sleep(2)

        # Find the elements containing the data you want
        data_elements = driver.find_elements(By.CSS_SELECTOR, cajas)

        # Extract the text from each element and print it
        for elem in data_elements:
            print(elem.text)


clickAndFetch(regionsBtns, boxes)
