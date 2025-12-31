# inventory = {'apple' : 45, 'banana' : 45, 'grapes' : 40}
# inventory.update({'grapes' : 105, 'orange' : 230})
# inventory.pop('apple')
# print (inventory)

# items = [3,5,7,9,11,13]
# items.pop(4)
# items.insert(1,11)
# print(items)

# first_set = {23,42,65,57,78,83,29}
# second_set = {57,83,29,67,73,43,48}
# final_set = first_set.symmetric_difference(second_set)
# print (final_set)

# first_set = {27,43,34}
# second_set = {34,93,22,27,43,53,48}
# if first_set.issubset(second_set) or first_set.issuperset(second_set):
#     first_set.clear()
#     print ("First set was a subset of second set, so it is cleared")
# elif second_set.issubset(first_set):
#     second_set.clear()
#     print ("Second set is a subset of the first set, so it is cleared")
# else:
#     print ("Neither are subsets of each other, so they're not cleared")

# months = {'jan':47, 'feb':52, 'march':47, 'april':44, 'may':52, 'june':53, 'july':54, 'aug':44, 'sept':54}
# list_month = list(months.values())
# list_month = list(set(list_month))
# print(list_month)

# sample_list = [87,45,41,65,94,41,99,94]
# remove = list(set(sample_list))
# tup = tuple(remove)
# print (tup)

# print ('a = A')
# print ('b = C')
# print ('c = B')
# print ('d = D')
# print ('e = F')
# print ('f = E')

club_A = {"Alice", "Bob", "Charlie"}
club_B = {"David", "Eve", "Bob"}
if club_A.intersection(club_B):
    print("That's an overlap!")