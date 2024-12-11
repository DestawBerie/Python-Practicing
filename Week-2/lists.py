#lists
#[milks, meat,cofee, sugar....]

shoping_lists=["milk", "meat", "coffee", "bread"]
print(shoping_lists)
print(len(shoping_lists))

nums=[1,2,3,4,5,6]
print(nums[0])
print(nums[2])
nums[2]=55
print(nums)
nums.pop()
print(nums)
nums.insert(0,22)
print(nums)

fruits=["banana", "orange", "lemon", "kiwi"]
print(fruits)
del fruits[1]


#combining lists
posetiv_numbers=[1,2,3,5,5,6]
zero=[0]
negative_nums=[-1,-2,-3,-5,-6]
intigers=negative_nums+zero+posetiv_numbers# output -1-2-3...0....123

intigers=negative_nums[::-1]+zero+posetiv_numbers# but the output of this oneis -6-5-..0 12345..good

print(intigers)

#we can also reverse the lists by using two methods
#::-1 and using .reverse method

#sorting is also
ages=[22,52,15,18,96,76,25]
ages.sort()
print(ages)
print