# Function to check if a year is a leap year
def is_leap_year(year):
    # A year is a leap year if it is divisible by 4, 
    # but not divisible by 100 unless it is also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input from the user
year = int(input("Enter a year: "))

# Check if it's a leap year and display the result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
