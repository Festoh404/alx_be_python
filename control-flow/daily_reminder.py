task = input("Task description: ").lower()
priority = input("Task's (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"

if time_bound == "yes":
     message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

print(message)
        
