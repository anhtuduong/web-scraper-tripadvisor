from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import pandas as pd

def get_reviews(url):
    # Do not use headless mode to allow you to interact with the browser
    options = webdriver.ChromeOptions()
    
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open the TripAdvisor page
    driver.get(url)
    
    # Wait for the user to manually solve the CAPTCHA
    input("Please solve the CAPTCHA in the browser, then press Enter to continue...")

    # Once the CAPTCHA is solved, continue with scraping
    time.sleep(3)  # Add a small delay to ensure the page has fully loaded

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    save_to_html(soup.prettify(), f"content.html")

    review_blocks = soup.find('section', id="REVIEWS")

    if not review_blocks:
        print("No more reviews found.")
        return
    
    save_to_html(review_blocks.prettify(), f"reviews/0.html")
    
    driver.quit()
    return reviews




def save_to_html(content, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved content to {filename}")

def save_to_csv(reviews, filename):
    df = pd.DataFrame(reviews)
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"Saved {len(reviews)} reviews to {filename}")

if __name__ == "__main__":
    attraction_url = "https://www.tripadvisor.com/Attraction_Review-g293924-d6786740-Reviews-Hanoi_Food_Tasting_Tours-Hanoi.html"
    reviews = get_reviews(attraction_url)
    save_to_csv(reviews, "tripadvisor_reviews.csv")
