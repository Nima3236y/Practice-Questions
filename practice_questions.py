import random

#1
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
n3 = int(input("Enter the third number: "))
if n2 < n3 and n1 < n3:
    print(f"{n3} is the largest number")
elif n1 < n2 and n3 < n2:
    print(f"{n2} is the largest number")
elif n2 < n1 and n3 < n1:
    print(f"{n1} is the largest number")
else:
    print("All three numbers are equal")

#2
months = (('January'), ('February'),('March'), ('April'), ('May'), ('June'), ('July'), ('August'), ('September'), ('October'), ('November'), ('December'))
num = int(input("Enter a number between 1 and 12: "))
if num > 12 or num < 1:
    print("Invalid number")
else:
    print(months[num - 1])

#3
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
temp = n1
n1 = n2
n2 = temp
print(f"After swapping, the first number is {n1} and the second number is {n2}")

#4
age = int(input("Enter your age: "))
mem = input("Are you a member? ").title()
if age < 12:
    print("Ticket is free for you")
elif age >=12 and age <= 60:
    if mem == 'Yes':
        print("Ticket price = rs.150")
    else:
        print("Ticket price = rs.200")
else:
    print("Ticket price = rs.100")

#5
usage = int(input("Enter power usage: "))
if usage <= 100:
    cost = usage*5
    print(f"Cost of power = Rs. {cost}")
elif 100 < usage <= 300:
    cost = (100*5) + ((usage - 100)*8)
    print(f"Cost of power = Rs. {cost}")
elif usage > 300:
    cost = (100*5) + (200*8) + ((usage - 300)* 10)
else:
    print("Invalid usage")

#6
moves = ['Rock', 'Paper', 'Scissors']
p1 = str(input("Enter your move: ")).title()
p2 = str(input("Enter your move: ")).title()
if p1 not in moves or p2 not in moves:
    print("Invalid input")
else:
    if p1 == moves[1] and p2 == moves[0]:
        print("Player 1 is the winner")
    elif p1 == moves[2] and p2 == moves[1]:
        print("Player 1 is the winner")
    elif p1 == moves[0] and p2 == moves [2]:
        print("Player 1 is the winner")
    elif p1 == p2:
        print("Draw")
    else:
        print("Player 2 is the winner")

#7
a = int(input("Enter the number of students in class A: "))
b = int(input("Enter the number of students in class B: "))
c = int(input("Enter the number of students in class C: "))
if a%2 == 0:
    first = a/2
else:
    first = float(a/2) + 0.5
    first = int(first)
if b%2 == 0:
    second = b/2
else:
    second = float(b/2) + 0.5
    second = int(second)
if c%2 == 0:
    third = c/2
else:
    third = float(c/2) + 0.5
    third = int(third)
total = first + second + third
print(f"Total requred number of desks is {total}")

#8
floor = 5
target = 3
if floor > target:
    print("Lift is going downwards")
elif floor < target:
    print("Lift is going upwards")
else:
    print("Lift will stay at the current floor")

#9
num = int(input("Enter a number: "))
if num < 0:
    print("The number is negative.")
elif num == 0:
    print("The number is 0.")
else:
    if num%2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")

#10
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
if n1 > n2:
    print(f"{n1} is greater than {n2}")
elif n1 < n2:
    print(f"{n2} is greater than {n1}")
else:
    if n1 > 0:
        print("The numbers are equal and positive")
    elif n2 < 0:
        print("The numbers are equal and negative")
    else:
        print("The numnbers are zero")

#11
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print ("Fizz Buzz")
elif num % 3 == 0 and num % 5 != 0:
    print ("Fizz")
elif num % 3 != 0 and num % 5 == 0:
    print ("Buzz")
else:
    print (num)

#12
facts = ['Flamingos turn pink from eating shrimp.',  "The only food that doesn't spoil is honey.", 'Shrimp can only swim backwards.', "A taste bud's life span is about 10 days.",  'It is impossible to sneeze while sleeping.', 'It is illegal to sing off-key in North Carolina.']
num = random.randint(0, 5)
if num == 0:
    print (facts[0])
elif num == 1:
    print (facts[1])
elif num == 2:
    print (facts[2])
elif num == 3:
    print (facts[3])
elif num == 4:
    print (facts[4])
else:
    print (facts[5])

#13
total = float(input("Enter total purchas amount: "))
mem = input("Are you a member? ").title()
if total > 1000:
    if mem == 'Yes':
        cost = total - (total*0.20)
        print (f"Final amount after 20% discount is Rs. {cost}")
    else:
        cost = total - (total*0.10)
        print (f"Final amount after 10% discount is Rs. {cost}")
else:
    print (f"Total cost is Rs. {total}")

#14
earth = float(input("Enter your weight on Earth: "))
planet = int(input("Enter a planet number(1-7): "))
gravities = [0.38, 0.91, 0.38, 2.53, 1.07, 0.89, 1.14]
if 1 <= planet <= 7:
    weight = earth * gravities[planet - 1]
    print (f"Your weight on {planet} will be {weight}")
else:
    print ("Invalid planet numebr")

#15
maths = float(input("Enter the marks of Maths: "))
science = float(input("Enter the marks of Science: "))
eng = float(input("Enter the marks of English: "))
nep = float(input("Enter the marks of Nepali: "))
percentage = (maths + science + eng + nep) / 4
print (f"Final grade = {percentage}")
if percentage > 70:
    print ("Distinctioin")
elif percentage > 60:
    print ("First")
elif percentage > 40:
    print ("Pass")
else:
    print ("Fail")

#16
cost = int(input("Enter the cost price of the bike: "))
if cost <= 50000:
    tax = cost*5/100
    print (f"The road tax for your bike is: {tax}")
elif 50000 < cost <= 100000:
    tax = cost*10/100
    print (f"The road tax for your bike is: {tax}")
elif cost > 100000:
    tax = cost*15/100
    print (f"The road tax for your bike is: {tax}")
else:
    print("Invalid cost price")

# 17
salary = int(input("Enter the Employee's salary: "))
years = int(input("Enter the amount of years they've worked: "))
if years > 10:
    bonus = salary + (0.10*salary)
    print(f"Their new salary is {bonus}")
elif 6 < years <= 10:
    bonus = salary + (0.6*salary)
    print(f"Their new salary is {bonus}")
elif years <= 6:
    bonus = salary + (0.5*salary)
    print(f"Their new salary is {bonus}")

#18
score = float(input("Enter the subject score"))
if 90 > score >= 100:
    print ("Congratulations! You have achieved exceptional grades.")
elif 50 <= score <= 90:
    print ("Your score is decent but I'd really suggest some improvement.")
elif score < 50:
    print ("I would highly recommend retaking the course.")
else:
    print ("Invalid Score!")

#19
age = int(input("Enter your age: "))
exp = int(input("How many years of experience do you have? "))
degree = input("Do you have a degree? ").strip().lower()
if degree == 'yes':
    degree = True
else:
    degree = False
if age >= 18:
    if degree is True:
        if exp > 3:
            print ("Highly Eligible")
        elif 1 < exp <= 3:
            print ("Eligible")
        else:
            print ("Under Review")
    else:
        print ("A degree is required in this Job")
else:
    print ("Sorry, you are not old enough to work here")

#20
gender = input("Enter M or F for your gender: ")
if gender != 'M' or gender != 'F':
    print ("Invalid input")
age = int(input("Enter your age: "))
if 18 <= age < 30:
    if gender == 'M':
        print ("Your wages are 700 a day")
    else:
        print ("Your wages are 750 a day")
elif 30 <= age <= 40:
    if gender == 'M':
        print ("Your wages are 800 a day")
    else:
        print ("Your wages are 850 a day")
elif age > 40:
    print ("You are too old to work here")
else:
    print ("You are too young to work")

#21
is_valid = True
balance = 50000
PIN =123
options = [1,2,3]
pin = int(input("Enter your PIN: "))
if pin == PIN:
    print("1. Withdraw \n2. Check Balance \n3. Exit")
    opt = int(input("Enter an option: "))
    if opt not in options:
        print ("Invalid option")
    else:
        if opt == 1:
            withdraw = int(input("How much would you like to withdraw? "))
            if withdraw > 50000:
                print ("Not enough money")
            else:
                money = balance - withdraw
                balance = balance - money
                print (f"Your current balance = {balance}")
        elif opt == 2:
            print (f"Your balance is {balance}")
        else:
            print ("Thank you for visiting")
else:
    print ("Invalid PIN")

#22
print("Welcome to the Magic Forest")
where = str(input("Where do you want to go? Norht or South? ")).strip().lower()
if where == 'south':
    print ("Game Over")
elif where == 'north':
    river = str(input("Do you want to cross the river or follow the path? ")).strip().lower()
    if river == 'cross the river':
        print ("Game Over")
    elif river == 'follow the path':
        choice = str(input("Choose between an Elf, a Fairy and an Ogre ")).strip().lower()
        if choice == 'ogre' or choice == 'fairy':
            print ("Game Over")
        elif choice == 'Elf':
            print ("You Win")
        else:
            print ("Invalid choice")
    else:
        print ("Invalid choice")
else:
    print("You can't go in those directions")

#23
print("Welcome to the Haunted House")
direction=input("Do you want to go 'upstairs' or 'downstairs'? ").strip().lower()
if direction=='downstairs':
    print("Game Over")
elif direction=='upstairs':
    choice=input("Do you want to 'enter the room' or 'stay outside'? ").strip().lower()
    if choice=='enter the room':
        print("Game Over")
    elif choice=='stay outside':
        creature=input("Choose between 'ghost', 'vampire', or 'werewolf': ").strip().lower()
        if creature=='ghost' or creature=='vampire':
            print("Game Over")
        elif creature=='werewolf':
            print("You Win")
        else:
            print("Invalid choice.")
    else:
        print("Invalid choice.")
else:
    print("Invalid direction.")