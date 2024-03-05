mytuple=tuple(("dave",22,True))


anothertupule=(1,3,5,7,9)


print(mytuple)
print(type(mytuple))
print(type(anothertupule))

newlist = list(mytuple)
newlist.append('dave')
newtupple=tuple(newlist)
print(mytuple)

(one,*two,hello)=anothertupule
print(one)
print(two)
print(hello)

 
print(anothertupule.count(9))





