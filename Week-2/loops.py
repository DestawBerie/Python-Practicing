print("happey new year")

for i in range(11):
  print(i)

countries=["finland", "ethiopia", "swedem", "norway"]
list_1st=[]
for country in countries:
    list_1st.append([country, countries])
    print(list_1st) 

for i in range(100):
   if i%2!=0:
      print(i)

nums=[0,1,2,3,-7,4,5]
for i in nums:
   if i<0:
      continue
   print(i)