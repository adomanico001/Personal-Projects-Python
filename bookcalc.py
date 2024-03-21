# Calculates how many book pages need to be read by target date
# @author Addie Domanico
# @version 1/21/2024

from datetime import datetime, timedelta

# Determines daily pages based off target date and current page
def calculate_daily_pages(total_pages, target_date, current_page):
    today = datetime.now().date()
    days_left = (target_date - today).days + 1

    if days_left <= 0:
        print("Invalid target date. Please enter a future date.")
        return

    remaining_pages = total_pages - current_page
    daily_pages = remaining_pages / days_left
    return daily_pages, remaining_pages

# User input and final calculation
def main():
    while True:
        try:
            total_pages = int(input("Enter the total number of pages in the book: "))
            current_page = int(input("Enter the page you're currently on: "))
            target_date_str = input("Enter the target date (YYYY-MM-DD): ")

            target_date = datetime.strptime(target_date_str, "%Y-%m-%d").date()

            formatted_target_date = target_date.strftime("%B %d")
        
            daily_pages, remaining_pages = calculate_daily_pages(total_pages, target_date, current_page)

            if daily_pages is not None and remaining_pages is not None:
                print(f"To finish the book by {formatted_target_date} you will need to read approximately {daily_pages:.2f} pages per day. You have {remaining_pages} pages left to read.")

            run_again = input("Do you want to calculate another book? (Y/N): ")
            if run_again.lower() not in ['y', 'Y', 'yes']:
                break

        # Checks if user entered valid input
        except ValueError:
            print("Invalid input. Please enter valid numbers and a valid date format.")

    print("Happy reading!")

if __name__ == "__main__":
    main()

        
    
