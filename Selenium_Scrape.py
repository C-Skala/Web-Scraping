from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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
scraper.get('https://webscraper.io/test-sites/e-commerce/static/computers/laptops')


#grab all laptops by class comp
unique_id = 1
while True:
    comps = scraper.find_elements(By.CLASS_NAME, "thumbnail")
    for comp in comps:
        comp_name = comp.find_element(By. CLASS_NAME, 'title')
        price = comp.find_element(By. CLASS_NAME, 'caption')
        specs = comp.find_element(By. CLASS_NAME, 'description')
        reviews = comp.find_element(By.CLASS_NAME, 'ratings')
        writer.writerow(
            [unique_id, comp_name.text, price.text, specs.text, reviews.text[:2]])
        unique_id += 1
        
    try:
        element = scraper.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/ul/li[13]/a')
        element.click()
    except:
        break
    
file.close()
scraper.quit()