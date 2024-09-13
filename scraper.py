from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
from selenium_stealth import stealth
import time
from bs4 import BeautifulSoup
import pandas as pd
import random

# ------------------------------

def get_reviews(driver, url):

    driver.get(url)
    
    # Wait for the user to manually solve the CAPTCHA
    input("Press Enter to continue...")

    # Once the CAPTCHA is solved, continue with scraping
    time.sleep(3)  # Add a small delay to ensure the page has fully loaded

    count = 1

    while True:

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        review_blocks = soup.find('section', id="REVIEWS")

        if not review_blocks:
            print("No more reviews found.")
            break
        
        save_to_html(review_blocks.prettify(), f"reviews/page_{count}.html")
        count += 1

        # Wait for the user to manually load more reviews
        input("Load more reviews and press Enter to continue...")
        time.sleep(3)
    
    driver.quit()


#  ------------------------------

def setup_driver():
    # WebDriver Options
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    
    # Setting Proxy 
    # proxy = "your.proxy.server:port"
    # options.add_argument(f'--proxy-server={proxy}')
    
    # Setting a User-Agent
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")
    
    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)
    return driver

def mimic_human_interaction(driver, url):
    driver.get(url)
    time.sleep(2)  # Wait for the page to load
    
    # Mimic human mouse movement and scrolling
    action = ActionChains(driver)
    body_element = driver.find_element_by_tag_name('body')
    action.move_to_element(body_element).perform()  # Move cursor to the body element
    time.sleep(1)  
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  
    time.sleep(2)

def save_to_html(content, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved content to {filename}")

def save_to_csv(reviews, filename):
    df = pd.DataFrame(reviews)
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"Saved {len(reviews)} reviews to {filename}")

# ------------------------------

if __name__ == "__main__":
    url = "https://www.tripadvisor.com/Attraction_Review-g293924-d6786740-Reviews-Hanoi_Food_Tasting_Tours-Hanoi.html"
    driver = setup_driver()
    get_reviews(driver, url)
