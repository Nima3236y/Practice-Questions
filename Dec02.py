# num = int(input("Enter a number: "))
# if (num > 0):
#     print (f"The number {num} is a positive number")
#     if (num % 2 == 0):
#         print(f"{num} is an even number")
#     else:
#         print(f"{num} is an odd number")
# elif (num < 0):
#     print (f"The number {num} is a negative number")
# else:
#     print ("The number is 0")

# n1 = int(input("Enter a number: "))
# n2 = int(input("Enter another number: "))
# if n1 > n2:
#     print (f"{n1} is greater than {n2}")
# elif n2 > n1:
#     print (f"{n2} is greater than {n1}")
# else:
#     if n1 > 0:
#         print (f"Both the numbers are equal and it is an positive number")
#     elif n1 < 0:
#         print (f"Both the numbers are equal and it is an negative number")
#     else:
#         print (f"Both the numbers are 0")

# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print ("Fizz Buzz")
# elif num % 3 == 0 and num % 5 != 0:
#     print ("Fizz")
# elif num % 3 != 0 and num % 5 == 0:
#     print ("Buzz")
# else:
#     print (num)

# maths = float(input("Enter the marks of Maths: "))
# science = float(input("Enter the marks of Science: "))
# eng = float(input("Enter the marks of English: "))
# nep = float(input("Enter the marks of Nepali: "))
# percentage = (maths + science + eng + nep) / 4
# print (f"Final grade = {percentage}")
# if percentage > 70:
#     print ("Distinctioin")
# elif percentage > 60:
#     print ("First")
# elif percentage > 40:
#     print ("Pass")
# else:
#     print ("Fail")

# cost = int(input("Enter the cost price of the bike: "))
# if cost <= 50000:
#     tax = cost*5/100
#     print (f"The road tax for your bike is: {tax}")
# elif 50000 < cost <= 100000:
#     tax = cost*10/100
#     print (f"The road tax for your bike is: {tax}")
# elif cost > 100000:
#     tax = cost*15/100
#     print (f"The road tax for your bike is: {tax}")

# salary = int(input("Enter the Employee's salary: "))
# years = int(input("Enter the amount of years they've worked: "))

# if years > 10:
#     bonus = salary + (0.10*salary)
#     print(f"Their new salary is {bonus}")
# elif 6 < years <= 10:
#     bonus = salary + (0.6*salary)
#     print(f"Their new salary is {bonus}")
# elif years <= 6:
#     bonus = salary + (0.5*salary)
#     print(f"Their new salary is {bonus}")

# purchase = int(input("Enter the total purchase amount: "))
# if purchase > 1000:
#     mem = input("Enter yes or no if you have membership or not: ").title()
#     if mem == 'Yes':
#         cost = purchase - (0.20*purchase)
#         print (f"Your total cost is {cost}")
#     elif mem == 'No':
#         cost = purchase - (0.10*purchase)
#     else:
#         print ("Invalid input")
# else:
#     print(purchase)


# earth = float(input("Enter your Earth weight:"))
# num = int(input("Enter your desired planet number: "))
# planets = [1:("Mercury", 0.38), 2:('Venus',0.91),3:('Mars', 0.38), 4:("Jupiter", 2.53), 5:('Saturn', 1.07), 6:("Uranus", 0.89), 7:('Neptune', 1.14)]
