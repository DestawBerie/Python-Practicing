#for the list case we can use append to add one item in the list
#and we can use extend to add many lists to the list

#every one is a programmer

time="six thirty"
if time=="five thirty":
   print("go to the class")

else:
   print("something else")


a= 10.2
if type(a)=="int":
  if a>0:
   print(f"{a} is a positive number")

  elif a<0:
   print(f"{a} is a Negative number")

  elif a==0:
   print(f" {a} is zero")

  else:
   print(f"{a}is not a number")

else:
 print("It is a float number")

 # short hand method or in other ways ternerry 
 
 a=10
 value="posetive" if a >0 else "negative"
 print(value)

 name="Destaw Mulusew Berie"
 value="Very long name" if len(name)>20 else "short name"
 print(value)

 # write a code to gradding of the students
 scor=95
 if scor>90:
   print("you grade is A")
 elif scor<90 and scor>80:
   print("your score is B")
 elif scor<80 and scor>70:
   print("your score is B+")
 elif scor<70 and scor>=60:
   print("your score is C")
 elif scor<60 and scor<=50:
   print("your score is D")
 else:
   print("your grade is lowest")