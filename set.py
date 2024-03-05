nums1= {1,2,3,4,5}
nums2= set((1,2,3,4 ))
print(nums1)
print(nums2)
print(type(nums1))
print(len(nums1))

#No duplicate are allowed

nums1={1,2,3,4}
print(nums1)
#True is a dupe of 1,False is a dupe of 0
nums1 ={1,True,2,False,3,4,0}
print(nums1)

#Check if any value is in the set
print(2 in nums1)

#But you cannot refer to an element in the set with an index position or i a key

#add a  new element to a set
nums1.add(8)
print(nums1)

#Add element from a set to another 
morenums1=(5,6,7)
nums1.update(morenums1)
print(nums1)

#You can update with list,tupules and dictionaries too

#Merge new sets to create new sets
one={1,2,3}
two={5,6,7}

newsets=one.union(two)
print(newsets)

#Keep only the duplicate
one={1,2,3}
two={2,3,4}

one.intersection_update(two)
print(one)

#Keep everything except the duplicate
one={1,2,3}
two={2,3,4}
one.symmetric_difference_update(two)
print(one)





 
