import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_reviews(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    }
    
    reviews = []
    page_num = 0
    
    while True:
        page_url = url + f"?page={page_num}"
        response = requests.get(page_url, headers=headers)
        
        if response.status_code != 200:
            print(f"Failed to retrieve data: {response.status_code}")
            break
        
        soup = BeautifulSoup(response.text, 'html.parser')
        review_blocks = soup.find_all('div', class_='review-container')
        
        if not review_blocks:
            print("No more reviews found.")
            break
        
        for block in review_blocks:
            review = {}
            review['title'] = block.find('a', class_='title').text.strip()
            review['rating'] = block.find('span', class_='ui_bubble_rating')['class'][1].split('_')[-1]
            review['date'] = block.find('span', class_='ratingDate')['title'].strip()
            review['content'] = block.find('p', class_='partial_entry').text.strip()
            
            reviews.append(review)
        
        print(f"Scraped page {page_num}")
        page_num += 1
        
        # To prevent getting blocked, you might want to include some delay
        time.sleep(2)  # delay for 2 seconds
    
    return reviews

def save_to_csv(reviews, filename):
    df = pd.DataFrame(reviews)
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"Saved {len(reviews)} reviews to {filename}")

if __name__ == "__main__":
    attraction_url = "https://www.tripadvisor.com/Attraction_Review-g293924-d6786740-Reviews-Hanoi_Food_Tasting_Tours-Hanoi.html"
    reviews = get_reviews(attraction_url)
    save_to_csv(reviews, "tripadvisor_reviews.csv")
