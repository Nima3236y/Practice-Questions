#1
i = 0
for i in range(5):
    i = i + 1
    if i%2 == 0:
        print (f'Number {i} is even')
    else:
        print (f'Number {i} is odd')

#2
list = [10,20,30,40]
sum = 0
for i in list:
    sum = sum + i
    print (f'Added {i}. Running total is {sum}')
print ('\n-------------------\n')
print (f'Toal Sum: {sum}')

#3
names = ["Ram", "Hari", "Sita"]
print ('---Email Greetings Generated---')
for name in names:
    print (f"Hi {name}, your course approval is ready!")

#4
chapters = [45,30,50,40]
count = 0
print ('---Book Chapter Summary---')
for i in chapters:
    count = count + 1
    print (f"Chapter {count} has {i} pages")

# #5
list = [4,5,3,2]
prod = 1
for i in list:
    prod = prod*i
print (prod)

#6
num = 11
for i in range(11):
    mul = num * i
    print (f'11 X {i} = {mul}')

#7
students = [

    {"name": "ram", "math_grade": 43},

    {"name": "hari", "math_grade": 65},

    {"name": "sita", "math_grade": 90}

]
for i in students:
    if i["math_grade"] >= 70:
        i["status"] = 'Approved'
    else:
        i["status"] = 'Rejected'
print (students)

#8
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
common = []
for i in list1:
    for j in list2:
        if i == j:
            common.append(i)
print ('These are the common elements: ',end = '')
print (common)

#9
list = [1,2,3,4]
for i in list:
    if i == 1 or i == 4:
        print(f'{i}', end = ' ')

#10
list = [1,2,3,4]
for i in list:
    if i == 1 or i == 2 or i == 4:
        print (i)

#11
list = [1,2,3,4]
list.pop(2)
list.insert(1,'a')
print(list)

#12
list = [1,2,3,4,5]
even = []
odd = []
for i in list:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print ('Even numbers are:', end = ' ')
print (even)
print ('Odd numbers are: ',end = '')
print (odd)

#13
num = int(input("Enter a number: "))
count = 0
for i in range(1, num+1):
    if num%i == 0:
        count += 1
if count > 2:
    print (f"Number {num} is not a prime number")
else:
    print (f"Number {num} is a prime number")

#14
list = [1,2,3,4,"a","b"]
alphabets = []
integers = []
for i in list:
    if type(i) == str:
        alphabets.append(i)
    else:
        integers.append(i)
print ('Strings are: ',end = '')
print (alphabets)
print ('Integers are:', end = ' ')
print (integers)

#15
string = str(input("Enter a string: "))
count = 0
for i in string:
    count = count + 1
print (f'There are {count} number of digits and letters in {string}')

#16
username = 'Das_real_Fuhrer'
password = 'Seig_Heil'
attempt = 3
given_user = str(input("Enter your username: "))
if given_user == username:
    for i in range(3):
        given_pass = str(input("Enter your password: "))
        if given_pass == password:
            print ("Access granted")  
        else:
            attempt -= i
            if attempt == 0:
                print ("Too many failed attempts, account is locked for 10 minutes")
            else:
                print (f"Incorrect password, please try again")
else:
    print ("Invali Username")

#17
num = int(input("Enter a number: "))
if num%2 == 0:
    print (f"Number {num} is an even number")
else:
    print (f"Number {num} is an odd number")

#18
num = int(input("Enter a number: "))
mul = 1
for i in range(1, num + 1):
    mul = mul * i
print (f"The factorial of {num} is {mul}")

#19
table = [1,2,3,4,5,6,7,8]
for i in table:
    for j in range(1, 11):
        print (f"{i} X {j} = {i * j}")
        print ("---------------")

#20
list = [1,2,3,4]
for i in list:
    if i == 1 or i == 2:
        print(i, end = ' ')

# 21
num = int(input("Enter a range: "))
sum = 0
for i in range(num):
    if i%2 != 0:
        sum = sum + i
print (f"The sum of odd numbers until {num} is {sum}")

#22
num = int(input("Enter a range: "))
sum = 0
for i in range(num):
    if i%2 == 0:
        sum = sum + i
print (f"The sum of even numbers until {num} is {sum}")

#23 
string = str(input("Enter a string: "))
count = 0
for i in string:
    if i == ' ':
        count = count + 1
print (f'There are {count} spaces in the string "{string}"')

#24
list = [1,2,3,4]
for i in range(len(list)):
    list[i] = list[i] * list[i] * list[i]
print (list)

#25
a = "programming"
rev = ""
for i in a:
    rev = i + rev
print (f"The reverse of {a} is {rev}")

#26
for i in range(50):
    print (i)
    if i == 7:
        break

#27
string = str(input("Enter a string: "))
for i in string:
    print (i)

#28
a = ["ram", "shyam",1,2]
for i in a:
    if type(i) == str:
        print (f"Hello! {i}", end = ' ')

#29
a = ["ram", "shyam",1,2]
list = []
for i in a:
    list.append('Dr.' + str(i))
print(list)

#30
list = [1,2,3,4,5]
new_list = []
for i in list:
    new_list.append(i*i)
print (new_list)

#31
list1 = [111,32,-9,-45,-17,9,85,-10]
posi_list = []
for i in list1:
    if i > 0:
        posi_list.append(i)
print (posi_list)

#32
list = [0,1,2,3,4,5,6]
for i in list:
    if i != 3:
        if i != 6:
            print (i)

#33
list = ["Real",33,"Nein",6.7]
type_of_list = []
for i in list:
    type_of_list.append(type(i))
print(type_of_list)

#34
count = 0
for i in range(3):
    count += i
print ("Done")

#35
for i in range(105, 1,-1):
    if i%7 ==0:
        print (i)

#36
bad_chars = [';',':','!','*']
string = "py;th* o:n ! ;py * t*h:o !n"
for i in string:
    if i in bad_chars:
        string = string.replace(i,'').replace(" ",'')
print (string)

#37
nums = [1,2,3,4,5,6,7,8,9,33,88,69,100]
even = 0
odd = 0
for i in nums:
    if i%2 == 0:
        even += 1
    else:
        odd = odd + 1
print (f"The number of even numbers is {even}")
print (f"The number of odd numbers is {odd}")

#38
sum = 0
for i in range(3, 99):
    if i%3 == 0 and i%5 == 0:
        sum = sum + i
print (f'The sum of multiples of 3 and 5 between 3 and 99 is {sum}')

#39
even = 0
odd = 0
for i in range (1, 100):
    if i%2 == 0:
        even = even + i
    else:
        odd = odd + i
print (f"The number of even numbers is {even}")
print (f"The number of odd numbers is {odd}")

#40
num = int(input("Enter a number: "))
rev = ""
num = str(num)
for i in num:
    rev = i + rev
if rev == num:
    print (f"{num} is a palindrome number")
else:
    print (f"{num} is not a palindrome number")

#41
num = str(input("Enter a number: "))
sum = 0
for i in num:
    i = int(i)
    sum = sum + (i**3)
num = int(num)
if num == sum:
    print (f"{num} is an armstrong number")
else:
    print (f"{num} is not an armstrong number")

#42
vowels = ['a','e','i','o','u']
string = str(input("Enter a string: "))
for i in string:
    if i in vowels:
        string.replace(i,"")
print (string)