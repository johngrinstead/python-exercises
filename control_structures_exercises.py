## Conditional Basics

# A. prompt the user for a day of the week, print out whether the day is Monday or not

day_of_week = input('What is today')

if day_of_week == 'Monday':
    print('Today is Monday')
    
else:
    print('Today is not monday')

# B. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day_of_week = input('What is today? ')

if day_of_week == 'Saturday' or day_of_week == 'Sunday':
    print('It is the weekend')
    
else:
    print('Today is a weekday')

# C. create variables and make up values for
#  -the number of hours worked in one week
#  -the hourly rate
#  -how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

hours_worked = int(input('How many hours did you work this week? '))

hourly_rate = int(input('How much is your hourly rate? '))

if hours_worked <= 40:
    weekly_paycheck = hours_worked * hourly_rate
    
else:
    weekly_paycheck = (40 * hourly_rate) + ((hours_worked - 40) * (hourly_rate * 1.5))

print(weekly_paycheck)


## While
# -Create an integer variable i with a value of 5.
# -Create a while loop that runs so long as i is less than or equal to 15
# -Each loop iteration, output the current value of i, then increment i by one.

i = 5

while i <= 15:
    print(i)
    i = i + 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

n = 0

while n <= 100:
    print(n)
    n = n + 2

# Alter your loop to count backwards by 5's from 100 to -10.

n = 100

while n >= -10:
    print(n)
    n = n - 5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

w = 2

while w <= 1_000_000:
    print(w)
    w = w ** 2

# Write a loop that uses print to create the output shown below.

# 100 95 90 85 80 75 70 65 60 55 50 45 40 35 30 25 20 15 10 5

l = 100

while l >= 5:
    print(l)
    l = l - 5


## For Loops

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

num = int(input('Provide a number '))

for number in range(1, 11):
     print(f'{num} x {number} = {number * num}')

## Create a for loop that uses print to create the output shown below.

# 1 22 333 4444 55555 666666 7777777 88888888 999999999

for number in range(1, 10):
    print(str(number) * number)

