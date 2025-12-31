#1
while True:
    age = input("Enter your age: ")
    if age == 'stop':
        break
    else:
        age = int(age)
        if 0 <= age < 18:
            print ("You are a minor.")
        elif 18 <= age <=60:
            print ("You are an adult.")
        elif age > 60:
            print ("You are a senior citizen.")
        else:
            print ("Invalid age")

#2
while True:
    vehicle = str(input("Enter a vehicle: ")).title()
    if vehicle == 'Bus':
        print ("finally, the wait is over.")
        break
    else:
        print ("waiting....")

#3
while True:
    fruit = str(input("Enter a fruit name: ")).title()
    if fruit == 'Apple':
        print ("You got it!")
        break
    else:
        print ("Try again")

#4
while True:
    password = str(input("Guess the password: "))
    if password == 'open sesame.':
        print ("Access granted!")
        break
    else:
        print ("Wrong password, try again.")

#5
ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
current_ratings = {}
i = 0
while i < len(ratings):
    if ratings[i] in current_ratings:
        current_ratings[ratings[i]]+=1
    else:
        current_ratings[ratings[i]] = 1
    i += 1
print (current_ratings)

#6
import random
num = random.randint(1, 10)
attempts = 0
while True:
    guess = int(input("Guess the number: "))
    if guess > num:
        print ("guess lower")
        attempts += 1
    elif num > guess:
        print ("guess higher")
        attempts +=1
    else:
        attempts += 1
        print (f"{guess} is the correct answer! It took you {attempts} tries to get it.")
        break

#7
username = 'admin'
password = '1234'
tries = 3
while tries != 0:
    input_username = str(input("Enter your username: "))
    input_password = str(input("Enter your password: "))
    if input_username == username and input_password == password:
        print ("Login successful.")
    elif input_username == username or input_password == password:
        print ("Invalid credentials, try again.")
        tries -= 1
    else:
        print ("Both are incorrect, try again.")
        tries -= 1
    if tries <1:
        print ("Too many failed attempts.")
        break

#8 
import random
while True:
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    mul = str(input(f"First number is {num1} and Second number is {num2}, Guess their multiple: "))
    if mul.lower() == 'exit':
        print ("Quiz ended.")
        break
    if mul.isdigit() and int(mul) == (num1 * num2):
        print ("Correct!")
    else:
        print ("Incorrect, try again.")

#9
count = 0
while True:
    num = input("Enter a number: ")
    if num == 'exit':
        break
    else:
        num = int(num)
        for i in range(1, num + 1):
            if (num % i) == 0:
                count += 1
        if count == 2:
            print (f'{num} is a prime number.')
        else:
            print (f'{num} is not a prime number.')
    count = 0

#10
secret = 'python'
while True:
    word = str(input("Guess the secret word: "))
    if word == secret:
        print ("Congratulations, you guessed the word!")
        break
    elif word == 'quit':
        break
    else:
        print ("Incorrect, try again,")

#11
count = 0
while True:
    name = str(input("Enter a name: ")).strip()
    if name == 'good luck':
        count += 1
        print (f"You have entered good luck {count} times.")
        if count == 3:
            print (f"You have typed good luck three times.")
            break

#12
starting = 1
while True:
    floor = input("Enter which floor do you want to go to: ").strip()
    if floor.isdigit():
        floor = int(floor)
        if floor == 0:
            print ("Goodbye, my friend")
            break
        if floor > starting:
            print ("Going upwards")
            starting = floor
        elif floor < starting:
            print ("Going downwards")
            starting = floor
        else:
            print ("The lift is already on that floor")
    else:
        print ("Floor can only be a positive digit.")

# Updated on 2025-12-31