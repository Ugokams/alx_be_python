task = input("Enter your task:")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print (f"REMINDER: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print (f"REMINDER '{task}' is a {priority} priority task. Plan to complete it as soon as possible!")

    case "medium":
        if time_bound == "yes":
            print (f"REMINDER: '{task}' is a {priority} priority task that needs to be completed by the set deadline.\n Please schedule time accordingly.")
        else:
            print (f"REMINDER: '{task}' is a {priority} priority task. Complete it when possible, preferably within a reasonable timeframe.")

    case "low":
        if time_bound == "yes":
            print(f"REMINDER: '{task}' is a {priority} priority task that needs to be completed by the set deadline.\n Please schedule time accordingly.")
        else:
            print(f"REMINDER: '{task}' is a {priority} priority task. Consider completing it when you have free time.")

    case _:
        print("You made an invalid entry")
