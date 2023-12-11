months_in_year = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
for month_name in months_in_year:
    print(month_name)
print("Months with names that have")
print("more than eight letters:")

for month_name in months_in_year:
    if len(month_name) > 8:
        print(month_name)
for num in range(5):
    print(num)
favorite_foods = []

for num in range(3):
    food=input("Please tell me a fav food: ")
    favorite_foods.append(food)
print("Thanks for sharing your favorite foods!")
for food in favorite_foods:
    print(food)
