fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]


# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())

# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruit = [fruit.upper() for fruit in fruits]

uppercased_fruit


# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

capitalized_fruits


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

def is_vowel(string):
    string = string.lower()
    return string in ["a", "e", "i", "o", "u"]
def count_vowels(string):
    count = 0
    for letter in string:
        if is_vowel(letter):
            count += 1
    return count
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if count_vowels(fruit) > 2]
print(fruits_with_more_than_two_vowels) #['guava', 'pineapple', 'mandarin orange']


# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

fruits_with_only_two_vowels = [fruit for fruit in fruits if count_vowels(fruit) == 2]

print(fruits_with_only_two_vowels)


# Exercise 5 - make a list that contains each fruit with more than 5 characters
more_than_five = [fruit for fruit in fruits if len(fruit) > 5]

more_than_five



# Exercise 6 - make a list that contains each fruit with exactly 5 characters

exactly_five = [fruit for fruit in fruits if len(fruit) == 5]

exactly_five


# Exercise 7 - Make a list that contains fruits that have less than 5 characters

less_than_five = [fruit for fruit in fruits if len(fruit) < 5]

less_than_five


# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

number_of_characters = [len(fruit) for fruit in fruits]

number_of_characters


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

fruits_with_letter_a = [fruit for fruit in fruits if fruit.count("a") >= 1]

fruits_with_letter_a


