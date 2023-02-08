from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import csv

#set up CSV
file = open('Laptops.csv', 'w')
writer = csv.writer(file)
writer.writerow(['id','name', 'price', 'specifications', 'number of reviews'])

#create chrome service and web driver instance

browser_driver = Service(r"C:\Users\cjska\OneDrive\Desktop\Dev Code Camp\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
scraper = webdriver.Chrome(service = browser_driver, options = options)

#Get the page
scraper.get('https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=1')
        
wait = WebDriverWait(scraper, 10)
popup = scraper.find_element(By.CLASS_NAME, 'acceptCookies')
wait.until(EC.visibility_of(popup))
popup.click()

#grab all laptops by class comp
unique_id = 1
x=2
page_runs = True
while True:
    comps = scraper.find_elements(By.CLASS_NAME, "thumbnail")
    for comp in comps:
        comp_name = comp.find_element(By.CLASS_NAME, 'title').get_attribute('title')
        price = comp.find_element(By. CLASS_NAME, 'caption')
        specs = comp.find_element(By. CLASS_NAME, 'description')
        reviews = comp.find_element(By.CLASS_NAME, 'ratings')
        writer.writerow(
            [unique_id, specs.text, price.text, specs.text, reviews.text[:2]])
        unique_id += 1
        
    try:
        
        #while page_runs ==True:
        #    if x != 20:
        #        scraper.get(f'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={x}')
        #        x+=1
        #    else:
        #        page_runs = False
            
        element = scraper.find_element(By.PARTIAL_LINK_TEXT, '›')
        element.click()
    except:
        break
    
file.close()
scraper.quit()