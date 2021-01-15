## 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(num):
    return num == 2 or num == '2'

is_two('2')


## 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(letter):
    return letter.lower() in ['a', 'e', 'i', 'o', 'u']

is_vowel('f')


## 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(letter):
    return is_vowel(letter) != True

is_consonant('d')


## 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

def capital_consonant(word):
    if is_consonant(word[0]) == True:
        print(word.capitalize())
    else:
        print(word)
        
capital_consonant('john')


## 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(percent, total):
    return total * (percent / 100)

calculate_tip (25, 70)


## 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(original_price, discount_percent):
    return original_price - (original_price * (discount_percent / 100))

apply_discount(70, 80)


## 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(number):
    return int(number.replace(',', ''))

handle_commas('1,234,456')


## 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(grade):
    if grade >= 90:
        print('A')
    elif grade >= 80:
        print('B')
    elif grade >= 70:
        print('C')
    elif grade >= 60:
        print('D')
    else:
        print('F')
        
get_letter_grade(99)


## 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(word):
    for letter in word:
        if is_vowel(letter) == True:
            return word.replace(letter, '')
        
remove_vowels('John')


## 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#-anything that is not a valid python identifier should be removed
#-leading and trailing whitespace should be removed
#-everything should be lowercase
#-spaces should be replaced with underscores
#for example:
    #-Name will become name

    #-First Name will become first_name

    #-% Completed will become completed

def normalize_name(name):
    name = name.strip()
    for letter in name:
        if letter == ' ':
            name = name.replace(letter, '_')
        elif letter.lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']:
            name = name.replace(letter, '')
    return name.lower()

normalize_name('    John Allen Grinstead !@#$$.  ')

## 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(numbers):
    sum = 0
    new_list = []
    
    for number in numbers:
        sum += number
        new_list.append(sum)
    return new_list
        
cumulative_sum([1,2,3,4])

