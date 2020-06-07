def is_year_leap(x):
    result = x / 4

    return result


year = int(input("Enter the year :"))
result = is_year_leap(year)
if result.is_integer():
    print("True")
else:
    print("False")

