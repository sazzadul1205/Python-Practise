# Practice#
# (1) The user will input his year of birth. You have to check if it's a leap-year.

print('Check if a year is a leap year or not')
year = int(input("Enter your year of birth: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# (2) The user will input a number. It should be calculated according to the grading system of your school/college/university and show the output of A+ or B- or F etc.

print('Grading system')
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Your grade is A+")
elif marks >= 80:
    print("Your grade is A")
elif marks >= 70:
    print("Your grade is B")
elif marks >= 60:
    print("Your grade is C")
elif marks >= 50:
    print("Your grade is D")
else:
    print("Your grade is F")