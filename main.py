import random
# The lists
destinations = ['London', 'Japan', 'Costa Rica']
restaurants = ['Ramen Hakata', '24 Hour Pizza' 'Chinese Place']
transportation = ['Bird', 'Plane', 'Superman', 'Car', 'Train', 'Walking']
entertainments = ['Bowling', 'Gaming', 'Staying Home', 'D&D']
# The functions
def random_destination():
    choice = random.choice(destinations)
    return choice

def random_restaurant():
    choice2 = random.choice(restaurants)
    return  choice2

def random_transportation():
    choice3 = random.choice(transportation)
    return choice3

def random_entertainment():
    choice4 = random.choice(entertainments)
    return choice4

# Testing things
destination = random_destination()
restaurant = random_restaurant()
mode23 = random_transportation()
entertainment = random_entertainment()

print(destination, restaurant, mode23, entertainment)