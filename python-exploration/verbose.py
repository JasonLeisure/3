###--------------AUTOMATE MY WEEK-----------####


# Verbose
def wakeUpEarly(day):
    if day == "Saturday" or day == "Sunday":
        return False
    elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        return True

print("Your Schedule: ")

def your_schedule(days_of_week):
    for day in days_of_week:
        if wakeUpEarly(day) == False:
            print("It's " + day + ", sleep in!")
            else:
                print("It's " + day + ", get up early!")

your_schedule(["Monday, "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
