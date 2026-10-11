# list=[10,20,20,30,40]
# #appending - adding values in last in list
# list.append(50)
# print(list)

# #list.insert(indexnumber,what value u want to add)
# #inserting value at any specfic index value and waha jaka print hoga and uss index pa pahala value thi usa right side shift kar dia , doesnt matter +ve and -ve indexing hoo usma bhi bhi right side shift  karega 
# list.insert(1,100)
# print(list)
# list.insert(55,99)
# print(list)
# list.insert(100,"praveen")
# print(list)
# list.insert(-5,"sumit")
# print(list)

# # extend()
# # when u have to multiple values in list at a time
# roll=[1,2]
# roll.extend([3,4,5,"abc","here we add roll number"])
# print(roll)

# #list.remove(value)
# #remove fucntion is used to remove values from list 
# #if same multiple value is prrsent then it will remove first appearence of that value by going from 0 to forward  indexing
# roll.remove(1)
# print(roll)
# roll.remove("abc")
# print(roll)

# #pop()
# # we use this to remove value from particular index
# list=[10,20,30,40,50]
# list.pop(2)
# print(list)
# # list.pop(200) here it will show index out of range becuzse . there is not value at index 200
# print(list)
# list.pop() # here if we dont give argument it will remove last value
# print(list)

# #variable(list).clear()
# # it will delete  all values inside list
# list.clear()
# print(list)

# #delete  (del) ye fucntion nhi hai ye ek reserve keyword
# list=[10,20,30,40,50]
# del list[1]
# print(list)
# del list[1:3]
# print(list)
# list.extend([45,23,67,233456,667342])
# print(list)
# del list[-5:-1]
# print(list)
# # del list[-324] error out of range
# print(list)
# print (10 in list)
# print (100 in list)
# print(50 not in list)

# # count function

# list=[10,20,30,10,30,50,20,70]
# print(list.count(10))
# print(list.count(100))

# # index() , yah hamlog input val;ue deta hai coloumn ke andar tabhi uss value ka index malum chalta hai
# # index , value ki index value provide karta hai , jo sabs pahala value match hoga indexing ke hisab se index 0 se start hoga
# print(list.index(20))

# # sort() function
# # sort the data value in ascending and for descending  order we give arguemnt (reverse=true)
# list.sort()
# print(list)                  
# list.sort(reverse=True)
# print(list)
# list1=["a", 'b' ,"wdhfb","3","z"]
# print(list1)
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)

list=[10,20,30,10,30,50,20,70]
del list[1:3]
print(list)
del list[:3]
print(list)

l = [10,20,30,40]
# l[100]=50  shows error becuase index is out of range
# print(l[4]) (so 50 will not print because it will not add)