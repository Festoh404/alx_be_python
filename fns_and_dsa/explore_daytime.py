import datetime


def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current_date}")

def calculate_future_date(days):
    future_date = datetime.date.today() + datetime.timedelta(days = days)
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    print(f"Future date: {formatted_future_date}")


def main():
    display_current_datetime()

    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(number_of_days)
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()
    
    
    

