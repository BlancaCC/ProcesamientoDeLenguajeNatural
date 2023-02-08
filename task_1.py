import json
with open('yelp_dataset/yelp_hotels.json', encoding='utf-8') as f:
    reviews = json.load(f)
f.close()
numReviews = len(reviews)
print(numReviews, 'reviews loaded')
print(reviews[0])
print(reviews[0].get('reviewerID'))