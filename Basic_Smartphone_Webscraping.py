from selenium import webdriver

from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "smartphones"
file = 1
for i in range (1,30):
    driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")
    elems = driver.find_elements(By.CLASS_NAME, "tUxRFH")
    print(f"{len(elems)} items found")
    if len(elems) == 0:
        driver.close()

    for elem in elems:
        d = elem.get_attribute("outerHTML")  
        with open(f"Smartphone_flipkart/ {query}_{file}.html","w",encoding="utf-8") as f:
            f.write(d) # type: ignore
            file +=1

    time.sleep(3)

driver.close()