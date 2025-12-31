# items = [1,2,3,4]
# i = 0
# while i < len(items):
#     if items[i] % 2 == 0:
#         print (items[i])
#         i += 1
#     else:
#         i += 1

#1
# total = 1
# num = int(input("Enter a positive number: "))
# while num > 0:
#     total += num
#     num = int(input("Enter a positive number: "))
# print (total)

# 2
# n = int(input("Enter a positive integer: "))
# while n > 1:
#     print (n)
#     n -= 1
#     if n == 1:
#         print ("Lower threshold reached")

# 3
# import random
# num = random.randint(1, 100)
# guess = 0
# while guess != num:
#     guess = int(input("Guess a number between 1 and 100: "))
#     if guess > num:
#         print ("Too high!")
#     elif guess < num:
#         print ("Too low!")
#     else:
#         print ("Congratulations")
#         break

#4
# length = 0
# while length < 8:
#     password = str(input("Enter a password: "))
#     if len(password) < 8:
#         print("Password must be 8+ characters")
#     else:
#         print ("Successfull")
#         break

#5
# total = 0
# counter = 1
# while counter < 51:
#     total += counter
#     counter += 1
# print (f"Final sum = {total}")

# 6
# num = int(input("Enter a number: "))
# n = 0
# while n < 10:
#     n += 1
#     print (f"{num} X {n} = {num*n}")

#7
# import random
# num = random.randint(1, 50)
# print (num)
# tries = 0
# while tries < 7:
#     guess = int(input("Guess the number: "))
#     if guess == num:
#         print ("!!!Congratulations!!!")
#         break
#     tries += 1
#     if tries == 7:
#         print ("No tries left")
#         break
#     print(f"You have {tries} left")

#8
rps = ["Rock","Paper","Scissors"]
p1_score = 0
p2_score = 0
while True:
    player1 = str(input("Enter Player1's move: ")).title()
    if player1 not in rps:
        print ("Invalid move")
        
    player2 = str(input("Enter Player2's move: ")).title()
    if player2 not in rps:
        print ("Invalid move")
        p1_score += 1
        
    if player1 == rps[0] and player2 == rps[2]:
        print ("Player1 is the winner")
        p1_score += 1
        
    elif player1 == rps[1] and player2 == rps[0]:
        print ("Player1 is the winner")
        p1_score += 1
        
    elif player1 == rps[2] and player2 == rps[1]:
        print ("Player1 is the winner")
        p1_score += 1
        
    elif player1 == player2:
        print ("Tie")

    else:
        print ("Player2 is the winner")
        p2_score += 1
    
    print (f"Player 1's score = {p1_score}")
    print (f"Player 2's score = {p2_score}")
    if p1_score == 5:
        print ("Player 1 is the winner")
        break
    if p2_score == 5:
        print ("Player 2 is the winner")
        break