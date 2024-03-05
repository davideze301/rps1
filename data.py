import math

# String data type
# literal assignment
first="david" 
last="ugonna"


# print (type(first))
# print(type(first)==str)
# print(isinstance(first,str ))




# construction function
pizza=str("pepperoni")
print (type(pizza))
print(type(pizza)==str)
print(isinstance(pizza,str ))


#concatenation function
fullname= first  +  ""  +   last
print(fullname)

fullname +="!"
print(fullname)

# casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement="i love pouded yam with egusi soup" + decade + "s"
print(statement)


#multiple lines
multiline='''
Hey,how are you?


I just want to  check up on you.
                               Thank you very much


'''
print(multiline)

#Escaping special characters
sentence ='I\'m back from Germany!\tHey!\n\nWhere\'s Where is your\\ location?'
print(sentence)
# strings method
# print(first)
# print(first.lower())
# print(first.upper()) 
# print(first)
 
print(last)
print(last.lower())
print(last.upper())
print(last)


print(multiline.title())
print(multiline.replace("good", "bad"))
print(multiline)


print(len(multiline))
multiline += "                                                 "
multiline ="                     " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.rstrip()))
print(len(multiline.lstrip()))

print("")
#Build a menu
title= "menu".upper()
print(title.center(20,"="))
print("cofee".ljust (16, ".")+ "$1".rjust(4))
print("cheese".ljust (16, ".")+ "$2".rjust(4))
print("chips".ljust (16, ".")+ "$3".rjust(4))
print("chicken".ljust (16, ".")+ "$4".rjust(4))
print("bread".ljust (16, ".")+ "$50".rjust(4))

print("")
#strings index values
print(first[1])
print(first[-1])
print(first[1:-1])
# some method return boolean data
print(first.startswith("d"))
print(first.endswith("a"))

#boolean data type
myvalue = True
x= bool(False)
print(type(x))
print(isinstance(myvalue,bool))


#numeric data type

#integar type
price=100
best_price=int(80)
print(type(price))
price=(isinstance(best_price ,int))



#float type
gpa=3.82
y=float(1.14)
print=(type(gpa))
print(round(gpa,1))



print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#casting a string to a number
zipcode ="10001"
zip_value= int(zipcode)

    







#built in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))
print(math.pi)









 