import json

# files names

hotel_file = 'yelp_dataset/yelp_hotels.json'
beauty_spas_file = 'yelp_dataset/yelp_beauty_spas.json'
restaurants_file = 'yelp_dataset/yelp_restaurants.json'

# Task 1.1: Loading all the hotel reviews from the Yelp hotel reviews file. 
print('Task 1.1')
with open(hotel_file, encoding='utf-8') as f:
    reviews = json.load(f)
f.close()
numReviews = len(reviews)
print(numReviews, 'reviews loaded')
print(reviews[0])
print(reviews[0].get('reviewerID'))
print('-'*10)

# Task 1.2 - optional [low difficulty]: loading line by line* the reviews from the Yelp beauty/spa resorts and restaurants reviews files
line_counter = 0
print('Task 1.2')
for file in [beauty_spas_file, restaurants_file]:
    with open(file, encoding='utf-8') as f:
        f.readline() # Ignoramos la primera línea que contiene [
        while f: 
            line = f.readline()
            # Aquí se haría el procesamiento
            print(line)
            break
            # Durante el procesamiento se detectará si es la última línea 
            # en tal caso se acabará el bucle
    f.close()

print('-'*10)

# Task 1.3 - optional [medium/high difficulty]: loading line by line* reviews on other domains (e.g.,movies, books, phones, digital music, CDs and videogames) from McAuley’s Amazon dataset2

print('Task 1.3')
amazon_file = 'yelp_dataset/All_Beauty.json'

with open(amazon_file, encoding='utf-8') as f:
    f.readline() # Ignoramos la primera línea que contiene [
    while f: 
        line = f.readline()
        # Aquí se haría el procesamiento
        print(line)
        break
        # Durante el procesamiento se detectará si es la última línea 
        # en tal caso se acabará el bucle
f.close()

print('-'*10)
