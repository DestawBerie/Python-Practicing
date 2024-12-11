letters="abcdefghijklmnopqrstuvwxyz"
vouwels="aeiou"
constonants="ancdfghjklmnpqrstvwxyz"
print(letters)
print(len(letters))
print(len(vouwels))
print(len(constonants))
print(letters.upper())
print(vouwels.upper())
print(constonants.upper())
print(dir(letters))

challange="30 Days of Python"
print(challange.upper())
print(challange.title())
print(challange.swapcase())
print(challange.find("0"))
print(challange.find("y"))


print(challange[0:2])
print(challange[2:])
print(challange[-2:])
print(challange[::-1])

print(challange.isupper())
print(challange.islower())

print(challange.count("0"))

city="mississippi"
print(city.count("i"))
print(city.count("s"))
print(city.find("i"))# the first i
print(city.rfind("i"))# the last one


#if we make a space at the first

city2=" mississippii"
print(city2)
print(city2.strip())
print("abac".isalpha())
print("12abac314".isalpha)
print("123".isdecimal)
print("123".isnumeric)

city3="mississippi"
print(set(city3))




