import sys

restaurant_file = sys.argv[1]
open_restaurant_file = open(restaurant_file)
restaurant_ratings_dictionary = {}

for restaurant_data in open_restaurant_file:
    restaurant_and_rating = restaurant_data.strip().split(':')
    restaurant_ratings_dictionary[restaurant_and_rating[0]] = restaurant_and_rating[1]

restaurant_strings = []

for restaurant, rating in restaurant_ratings_dictionary.items():
    restaurant_strings.append("{} is rated at {}.".format(restaurant, rating))

for string in sorted(restaurant_strings):
    print string
    
open_restaurant_file.close()