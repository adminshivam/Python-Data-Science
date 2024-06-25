# Lists

users = ['shivam', 'harsh', 'sandeep', "Ayush", "Shefali"]
data = ['shivam', 1, 2.2, 'random']
emptyList = []

print(type(users))

# key = str.lower used to include lowercase characters
users.sort(key=str.lower)
print(users)

print(len(users))

users.extend(data)

print(users)

# print from 0 to 1 excluding 2 
print(users[0:2])

# print whole list of users
print(users[:])


# copy list
copyList = list(users)
copyList2 = users[:]

copyList2.reverse()
print(copyList2)

copyList2.clear()

print("Printing copyList2")
print(copyList2)

del copyList2
# error as we have just deleted the list
print(copyList2)