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


