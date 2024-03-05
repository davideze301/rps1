#dictionary
band = {
"vocals": "plant",
"guitar": "page",
    
}
band2 = dict(vocals="plant",guitar="page") 

print(band)
print(band2)
print(type(band))
print(len(band))


# Access items
print(band["vocals"])
print(band.get("guitar"))



#list all key
print(band.keys())
#list all values
print(band.values())

#list of key/values pairs as tupules
print(band.items())

#verify if a key exist
print("guitar"  in band)
print("triangle"  in band)

#change value
band["vocal"]="coverdale"
band.update({"bass":"jpj"})
print(band)
#removing values
print(band.pop("bass"))
print(band)


band["drums"] = "bonham"
print(band)


print(band.popitem())#tupule
print(band)
#delete and clear
band["drums"]="bonham"
del band ["drums"]
print(band)

band2.clear()
print(band2)
del  band2


#copy dictionary
# band2 =band #create a refrence
# print("bad copy!")
# print(band2)
# print(band) 
# band2["drums"]="david"
# print(band)
 
band2=band.copy()
band2["drums"]="david"
print("Good copy!")
print(band)
print(band2)


# or use the dict() construction function
band3=dict(band)
print("Good copy!")
print(band3)

#Nested dictionaries
member1 ={
    "Name":"plant",
    "Instrument": "vocals"
    }
member2 ={
    "Name":"page",
    "Instrument": "guitar"
    }
band ={
    "member1" : member1,
    "member2" : member2,
}
print(band["member1"],["name"])






