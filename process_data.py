from bs4 import BeautifulSoup
import pandas as pd

# ------------------------------

def save_to_csv(reviews, filename):
    df = pd.DataFrame(reviews)
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"Saved {len(reviews)} reviews to {filename}")

def process_reviews_from_html(html_file):
    soup = BeautifulSoup(html_file, 'html.parser')
    review_blocks = soup.find_all('div', attrs={'class': '_c', 'data-automation':'reviewCard'})
    
    if not review_blocks:
        print("No reviews found.")
        return []
    
    reviews = []
    for review in review_blocks:
        # Title
        title = review.find('div', attrs={'class': 'biGQs _P fiohW qWPrE ncFvv fOtGX'}).find('a', attrs={'class': 'BMQDV _F Gv wSSLS SwZTJ FGwzt ukgoS'}).find('span', attrs={'class': 'yCeTE'}).text.strip()

        # Content
        content = review.find('span', attrs={'class': 'JguWG'}).find('span', attrs={'class': 'yCeTE'}).text.strip()

        # Date
        date = review.find('div', attrs={'class': 'TreSq'}).find('div', attrs={'class': 'biGQs _P pZUbB ncFvv osNWb'}).text.strip().split('Written ')[1]

        # Score
        score = review.find('svg', attrs={'class': 'UctUV d H0'}).find('title').text.strip().split(' of 5 bubbles')[0]

        # Username
        username = review.find('div', attrs={'class': 'zpDvc Zb'}).find('span', attrs={'class': 'biGQs _P fiohW fOtGX'}).find('a', attrs={'class': 'BMQDV _F Gv wSSLS SwZTJ FGwzt ukgoS'}).text.strip()

        # Location and Contribution
        location_and_contribution = review.find('div', attrs={'class': 'zpDvc Zb'}).find('div', attrs={'class': 'JINyA'}).find('div', attrs={'class': 'biGQs _P pZUbB osNWb'}).find_all('span')

        if len(location_and_contribution) == 2:
            location = location_and_contribution[0].text.strip()
            contribution = location_and_contribution[1].text.strip().split(' contribution')[0]
        else:
            location = None
            contribution = location_and_contribution[0].text.strip().split(' contribution')[0]

        # Travel with
        travel_with = review.find('div', attrs={'class': 'RpeCd'})
        if travel_with:
            travel_with = travel_with.text.strip().split('• ')
            if len(travel_with) > 1:
                travel_with = travel_with[1]
            else:
                travel_with = None
        else:
            travel_with = None

        # Review of
        review_of = review.find('div', attrs={'class': 'biGQs _P pZUbB xUqsL mowmC KxBGd'})
        if review_of:
            review_of = review_of.find('a', attrs={'class': 'BMQDV _F Gv wSSLS SwZTJ FGwzt suezE'}).text.strip().split('Review of: ')[1]
        else:
            review_of = None

        reviews.append({
            'Title': title,
            'Content': content,
            'Date': date,
            'Score': score,
            'Username': username,
            'Location': location,
            'Contribution': contribution,
            'Travel with': travel_with,
            'Review of': review_of
        })
    return reviews

# ------------------------------
if __name__ == "__main__":

    total_reviews = []
    for i in range(1, 206):
        html_file = open(f"reviews/page_{i}.html", 'r', encoding='utf-8').read()
        reviews = process_reviews_from_html(html_file)
        print(f"Processed {len(reviews)} reviews from page {i}")
        total_reviews.extend(reviews)
    save_to_csv(total_reviews, "reviews.csv")