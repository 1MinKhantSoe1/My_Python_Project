"""
Exercise 1: How much is your sleep debt?

    This program is calculate 5 days of the total hours of sleep and sleep-debt for user. If user is sleep over 40 hours
    this message will show "You are getting enough sleep. Lucky!" or not this message will show "Your sleep debt over
    this time is: (user sleep debt hours) You need more sleep!".

    The program workflow are follow:

        1. User need to enter how many hour of sleep in each 5 days.

        2. The program will calculate total hours of sleep.

        3. Show total hours of sleep to user.

        4. If total hours of sleep is less than 40 hours this message will show "Your sleep debt over
           this time is: (user sleep debt hours) You need more sleep!".

        5. If total hours of sleep is greater than 40 hours this message will show "You are getting enough sleep. Lucky!
           ".
"""


def main():

    print("This program will calculate your sleep-debt over 5 days.")

    # User input start here
    day_1_sleep = int(input("Please Enter Day 1 sleep: "))
    day_2_sleep = int(input("Please Enter Day 2 sleep: "))
    day_3_sleep = int(input("Please Enter Day 3 sleep: "))
    day_4_sleep = int(input("Please Enter Day 4 sleep: "))
    day_5_sleep = int(input("Please Enter Day 5 sleep: "))
    # User input end here

    total_hours_of_sleep = day_1_sleep + day_2_sleep + day_3_sleep + day_4_sleep + day_5_sleep  # Total hours of sleep

    print("Your total hours of sleep were:")
    print(total_hours_of_sleep)  # Show total hours of sleep to user

    if total_hours_of_sleep < 40:  # If total hours of sleep is less than 40 hours this will true

        sleep_dept = abs(total_hours_of_sleep-40)  # total sleep debt

        """Total sleep debt message will show"""
        print("Your sleep debt over this time is:")
        print(sleep_dept, "hours")
        print("You need more sleep!")

    else:  # If user sleep over 40 hours in 5 days this condition will true and message will show

        print("You are getting enough sleep. Lucky!")


main()
