age = 23
cash_on_hand = 5

if age > 17 and cash_on_hand > 8:
    print("You can buy a lottery ticket.")
    print("How many would you like?")
else:
    print("You may not buy a lottery ticket.")
    print("Can I interest you in some candy?")

print("Thank you for your patronage.")
age = 19

if age > 12 and age < 20:
    is_teenager = True
else:
    is_teenager = False

if is_teenager:
    print("Are you on TikTok?")
else:
    print("Are you on Facebook?")

this_is_false = 3 < 2
print(this_is_false)
if "":
    print("Empty string is considered true")
else:
    print("Empty string is considered false")

if 0:
    print("0 is considered true")
else:
    print("0 is considered false")

age = 23
cash_on_hand = 5

if age > 17 and cash_on_hand > 8:
    print("You can buy a lottery ticket.")
    print("How many would you like?")
elif age > 17 and cash_on_hand <= 8:
    print("You don't have enough money.")
    print("Please, come back when you get more.")
else:
    print("You may not buy a lottery ticket.")
    print("Can I interest you in some candy?")

print("Thank you for your patronage.")
