print("Hello New Person!")
name = input("What is your name? ")
print("Hello " + name)
birth_month = input("Enter your birth month in numerical form: ")
month = int(birth_month)
print(month)
birth_day = input("Enter your birth day: ")
day = int(birth_day)
print(day)
birth_year = input("Enter your birth year: ")
age = 2023 - int(birth_year)
print(age)
from datetime import date
 
def calculateAge(birthDate):
    days_in_year = 365.2425   
    age = int((date.today() - birthDate).days / days_in_year)
    return age
         
print(calculateAge(date(1999, 10, 13)), "years old")
if int(age) == 18:
  int(age) == 18
  print("You are 18")
else:
  print("You are 18 0r older than 18!")
weight = int(input("Weight: "))
unit = input("(k)g or (L)bs: ")
if unit.upper() == "K":
  converted = weight / 0.45
  print("Weight in Lbs: " + converted)
else:
  converted = weight * 0.45
  print("Weight in Kgs: " + str(converted))