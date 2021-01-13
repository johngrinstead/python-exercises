## You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?


price = 3

little_mermaid = 3

bear_brother = 5

hercules = 1

total = (little_mermaid + bear_brother + hercules) * price

print(total)


## Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google_pay = 400

amazon_pay = 380

facebook_pay = 350

facebook_hrs = 10

google_hrs = 6

amazon_hrs = 4

total_pay = (google_pay * google_hrs) + (amazon_pay * amazon_hrs) + (facebook_pay * facebook_hrs)

print(total_pay)


## A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

class_not_full = True

no_schedule_conflict = True

can_enroll = class_not_full and no_schedule_conflict

can_enroll


## A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

premium_member = True

number_of_items = 5

offer_not_expired = True

can_apply_offer = (number_of_items > 2 or premium_member) and offer_not_expired

can_apply_offer

##########################################

username = 'codeup'
password = 'notastrongpassword'


#############################################

## the password must be at least 5 characters

is_long_enough = len(password) >= 5

is_long_enough


## the username must be no more than 20 characters

username_short_enough = len(username) <= 20

username_short_enough


## the password must not be the same as the username

unique_password_username = password != username

unique_password_username


## bonus neither the username or password can start or end with whitespace

username_whitespace = (username[0] != ' ') and (username[-1] != ' ')

password_whitespace = (password[0] != ' ') and (password[-1] != ' ')

username_whitespace

password_whitespace


