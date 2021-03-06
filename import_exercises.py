## Import and test 3 of the functions from your functions exercise file.
#Import each function in a different way:
# -import the module and refer to the function with the . syntax
# -use from to import the function directly
# -use from and give the function a different name

import function_exercises

function_exercises.apply_discount(89, 25)

############################################

import function_exercises as fe

fe.handle_commas('123,123,123')

######################################

from function_exercises import get_letter_grade

get_letter_grade(78)

#################################################

## 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

import itertools as it
len(list(it.product([1, 2, 3], 'abc')))


## 2. How many different ways can you combine two of the letters from "abcd"?

len(list(it.combinations('abcd', 2)))

#############################################
#############################################

# A. Total number of users

len(profiles)

# B. Number of active users

count = 0 

for user in profiles:
    if user['isActive'] == True:
        count = count + 1
print(count)

# C. Number of inactive users

count = 0 

for user in profiles:
    if user['isActive'] == False:
        count = count + 1
print(count)


# D. Grand total of balances for all users

total = 0

balances = []

balance_float = []

for user in profiles:
    balances.append(user['balance'])
    
for balance in balances:
    balance = balance.replace('$', '')
    balance = balance.replace(',', '')
    balance = float(balance)
    balance_float.append(balance)
    
grand_total = sum(balance_float)

print(grand_total)


# E. Average balance per user

avg_total = sum(balance_float) / len(balance_float)

print(round(avg_total, 2))


# F. User with the lowest balance

lowest_balance = profiles[0]['balance']

lowest_balance_user = profiles[0]['name']

for user in profiles:
    if user['balance'] < lowest_balance:
        lowest_balance = user['balance']
        lowest_balance_user = user['name']

print(lowest_balance_user)
print(lowest_balance)


# G. User with the highest balance

highest_balance = profiles[0]['balance']

highest_balance_user = profiles[0]['name']

for user in profiles:
    if user['balance'] > highest_balance:
        highest_balance = user['balance']
        highest_balance_user = user['name']
        
print(highest_balance_user)
print(highest_balance)


# H. Most common favorite fruit

from collections import Counter

favorite_fruits = []



for user in profiles:
    favorite_fruits.append(user['favoriteFruit'])
    most_favorite_fruit = max(Counter(favorite_fruits))
    
print(most_favorite_fruit)

# I. Least most common favorite fruit

least_most_favorite = min(Counter(favorite_fruits))

print(least_most_favorite)


# J. Total number of unread messages for all users

greetings = []

amount_of_messages = []

total_messages = 0

for user in profiles:
    greetings.append(user['greeting'])
    
for greeting in greetings:
    amount_of_messages = [int(i) for i in greeting.split() if i.isdigit()]
    for n in amount_of_messages:
        total_messages = total_messages + n

    
print(total_messages)


