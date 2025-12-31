# password = 'BerserkIDK'
# print (password.count('B'))
# print (password.replace('k','0').replace('K','0'))
# conversion = password.maketrans('e','0')
# print(password.translate(conversion))

# full_name = '   rs   m123'
# result = full_name.strip()
# final_result = result.replace(" ","")
# print(final_result)
# print(''.join(final_result))

# startswith endswith find index find pindex

# phone_number = '+9779803456789'
# result = phone_number.startswith('+977')
# print(result)

# image = 'Image.jpg'
# result = image.endswith('.jpg')
# print(result)

# domain_name = 'grozny123@gmail.com'
# result = domain_name.find('x')
# print(result)

# domain_name = 'grozny123@gmail.com'
# result = domain_name.index('y')
# print(result)

# domain_name = 'grozny123@gmail.com'
# result = domain_name.rindex('y') - len(domain_name)
# print(result)

# full_name = input("Enter your full name: ")
# name = full_name.lower().strip().split() 
# name = '_'.join(name)
# print(f"Your name is {name}")

# secret_password = input("Enter your passowrd: ")
# password = secret_password.lower().replace("a","@").replace("e","3").replace("i","!").replace("o","0").replace("s","S")
# print (f"Your secret agent code is {password}0##9") #maketrans is better for this task

# num = input("Enter your phone number:")
# num = num.replace(" ","").replace("-","").replace("(","").replace(")","")
# print(f"Your clean number: {num}")

name = input("What is your name? ")
print(f"Your name is {name.title()}")