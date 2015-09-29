import sys

restaurant_file = sys.argv[1]
open_restaurant_file = open(restaurant_file)
restaurant_ratings_dictionary = {}

for restaurant_data in open_restaurant_file:
    restaurant_and_rating = restaurant_data.strip().split(':')
    restaurant = restaurant_and_rating[0]
    rating = restaurant_and_rating[1]
    restaurant_ratings_dictionary[restaurant] = rating
    
for restaurant, rating in sorted(restaurant_ratings_dictionary.items()):
    print "{} is rated at {}.".format(restaurant, rating)
    
open_restaurant_file.close()