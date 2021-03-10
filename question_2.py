# 2. Write an if statement to determine whether a variable holding a year is
# a leap year.

var_year = 2100

if var_year % 400 == 0:
    print("a leap year")

elif var_year % 4 == 0:
    if var_year % 100 != 0:
        print(" a leap year")
    else:
        print("Not leap year")
else:
    print("Not a leap year")
