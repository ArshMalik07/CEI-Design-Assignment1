def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year =int(input("Enter year: "))
if year >=0:
    if is_leap_year(year):
        print(f"{year} is leap year")
    else:
        print(f"{year} is not a leap year.")
else:
    print("Invalid year")