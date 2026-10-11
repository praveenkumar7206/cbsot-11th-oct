# SET  

# remove duplicates character from string without using set 

s = "asndsdvhbgadhew"
s1=""
for i in s :
  if i not in s1:
    s1 = s1+i
print(s1) 

s2= {21,35,21,34323,42}

for ch in s2:
  print(ch)
#add
s2.add(87)
print(s2)
#remove
s2.remove(21)
print(s2)
#copy
s3=s2.copy()

#updation
s2.update

l = [10,20,30,40]
# l[100]=50  shows error becuase index is out of range
# print(l[4]) (so 50 will not print because it will not add)







