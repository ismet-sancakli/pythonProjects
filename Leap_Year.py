

year = int(input("Which year do you want to check? "))

if (year % 400 == 0):
  print(f"Year is {year} , This year is Leap Year")
elif (year % 4 == 0 and year % 100 != 0):
  print(f"This year {year} is leap")
else:
  print(f"Year {year} is not leap year")


