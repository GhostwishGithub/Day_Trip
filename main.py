import random
# The lists
destinations = ['London', 'Japan', 'Costa Rica', 'North Korea', 'a literal trash can']
restaurants = ['Ramen Hakata', '24 Hour Pizza' 'some random-ass chinese place', 'dumpster behind the Waffle House']
transportation = ['a bird', 'a plane', 'Superman', 'a rental car', 'a stolen car' 'a train', 'walking', 'getting shot out of a cannon', 'a TIE fighter']
entertainments = ['bowling', 'gaming', 'staying home', 'D&D', 'just die', 'gladiator duels', 'deafening flatulence']
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

print(f"Looks like you're going to {destination}. That sound good to you? y/n:")
user_feedback = input()
while user_feedback == 'n':
    destination = random_destination()
    print(f"Ah, okay, then how about {destination}? y/n:")
    user_feedback = input()
print(f"Great. Now that's settled, it seems you'll be eating at {restaurant}. Sound good? y/n")
user_feedback = input()
while user_feedback == 'n':
    restaurant = random_restaurant()
    print(f"Ah, okay, then how about {restaurant}? y/n:")
    user_feedback = input()
print(f"Okay, hope you don't get tape worms. Now, as for transporation, how does {mode23} sound? y/n")
user_feedback = input()
while user_feedback == 'n':
    mode23 = random_transportation()
    print(f"Ah, okay, then how about {mode23}? y/n:")
    user_feedback = input()