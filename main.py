import random
# The functions
def random_random(list):
    result = random.choice(list)
    return result

# def random_destination():
#     destinations = ['London', 'Japan', 'Costa Rica', 'North Korea', 'a literal trash can']
#     choice = random.choice(destinations)
#     return choice

# def random_restaurant():
#     restaurants = ['Ramen Hakata', '24 Hour Pizza', 'some random-ass chinese place', 'the dumpster behind the Waffle House']
#     choice2 = random.choice(restaurants)
#     return  choice2

# def random_transportation():
#     transportation = ['a bird', 'a plane', 'Superman', 'a rental car', 'a stolen car', 'a train', 'walking', 'getting shot out of a cannon', 'a TIE fighter']
#     choice3 = random.choice(transportation)
#     return choice3

# def random_entertainment():
#     entertainments = ['bowling', 'gaming', 'staying home', 'D&D', 'just suddenly dying', 'gladiator duels', 'deafening flatulence']
#     choice4 = random.choice(entertainments)
#     return choice4

# def other_random(function):
#     user_feedback = 'n'
#     while user_feedback == 'n':
#         function = random_random(function)
#         print(f"Then what about {function}? y/n")
#         user_feedback = input()
#     return function

# def destination_picker(destination):
#     print(f"Looks like you're going to {destination}. That sound good to you? y/n:")
#     user_feedback = input()
#     while user_feedback == 'n':
#         destination = random_destination()
#         print(f"Ah, okay, then how about {destination}? y/n:")
#         user_feedback = input()
#     return destination

# def restaurant_picker(restaurant):
#     print(f"Great. Now that's settled, it seems you'll be eating at {restaurant}. Sound good? y/n")
#     user_feedback = input()
#     while user_feedback == 'n':
#         restaurant = random_restaurant()
#         print(f"Ah, okay, then how about {restaurant}? y/n:")
#         user_feedback = input()
#     return(restaurant)

# def transportation_picker(mode23):
#     print(f"Okay, hope you don't get tape worms. Now, as for transporation, how does {mode23} sound? y/n")
#     user_feedback = input()
#     while user_feedback == 'n':
#         mode23 = random_transportation()
#         print(f"Ah, okay, then how about {mode23}? y/n:")
#         user_feedback = input()
#     return(mode23)

# def entertainment_picker(entertainment):
#     print(f"Right, okay, last question: entertainment. Would you like to partake in {entertainment}? y/n")
#     user_feedback = input()
#     while user_feedback == 'n':
#         entertainment = random_entertainment()
#         print(f"Ah, okay, then how about {entertainment}? y/n:")
#         user_feedback = input()
#     return(entertainment)
def main():
    destinations = ['London', 'Japan', 'Costa Rica', 'North Korea', 'a literal trash can']
    restaurants = ['Ramen Hakata', '24 Hour Pizza', 'some random-ass chinese place', 'the dumpster behind the Waffle House']
    transportation = ['a bird', 'a plane', 'Superman', 'a rental car', 'a stolen car', 'a train', 'walking', 'getting shot out of a cannon', 'a TIE fighter']
    entertainments = ['bowling', 'gaming', 'staying home', 'D&D', 'just suddenly dying', 'gladiator duels', 'deafening flatulence']
    destination = random_random(destinations)
    restaurant = random_random(restaurants)
    mode23 = random_random(transportation)
    entertainment = random_random(entertainments)
    # other_random(destination)
    # other_random(restaurant)
    # other_random(mode23)
    # other_random(entertainment)
    user_feedback = 'n'
    while user_feedback == 'n':
        print(f"Okay, so, you're going to go {destination} via {mode23} to eat at {restaurant} before engaging in some {entertainment}. Everything look good? y/n")
        user_feedback = input()
        if user_feedback == 'n':
            print(f"You know, I would have slapped most users clear across the room by now, so you better be glad you're cute. Allright. Using 1-4 and no bananas, tell me which one you want to redo: 1. {destination} 2. {restaurant} 3. {mode23} 4. {entertainment}")
            user_feedback = input()
            if user_feedback == '1':
                destination = random_random(destinations)
                user_feedback = 'n'
            elif user_feedback == '2':
                restaurant = random_random(restaurants)
                user_feedback = 'n'
            elif user_feedback == '3':
                mode23 = random_random(transportation)
                user_feedback = 'n'
            elif user_feedback == '4':
                entertainment = random_random(entertainments)
                user_feedback = 'n'
            else:
                print("THAT'S IT I QUIT!!!!")
                user_feedback = 'n'
    else:
        print(f"Great! So you're going to {destination} via {mode23} to eat at {restaurant} before engaging in some {entertainment}. Enjoy your trip!")
main()