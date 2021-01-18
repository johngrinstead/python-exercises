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


