users = ["David", "ugonna", "eze"]  # Changed from tuple to list
data = ("David", 23, True)
emptylist = []

print("David" in emptylist)
print(users[0])
print(users[-2])
print(users.index("eze"))
print(users[0:2])
print(users[0:1])
print(users[0:3])
print(users[-3:-1])

print(len(data))
users.append('Smith')
print(users)
users += ['victoria']
print(users)
users.extend(['ihuomachukwu','jason'])
print(users)
# users.extend('data')
# print(data)



users.insert(0,'Jarmaine')
print(users)


users[2:2]=['Eddie','wilfred']
print(users)


users[2:3]=['robert','beratheon']
print(users)

users[1:3]=['joy','olamiposi']
print(users)

users.remove('jason')
print(users)


print(users.pop())
print(users)

del users[0]
print(users)


# del data

print(data)

users[1:2]=["david"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4,24,75,6,10]
nums.reverse
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums,reverse=True))
print(nums)


numscopy=nums.copy()
mynums=list(nums)
mycopy=nums[:]


print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)


print(type(nums))

