list=["cat","dog","tiger","elephant","rat","orange","grapes","banana","five","python"]

#Create a dictionary group word a/c to their length
#Find length having maximum number of words
#Now print the word in the found length having maximum vowels

dict={}

for i in list:
    length=len(i)

    if length not in dict:
        dict[length]=[i]
        
    
    else:
        dict[length].append(i)
        

for key,value in dict.items():
    print(key,"->",value)
    
max=0
for key,value in dict.items():
    l=len(value)
    if l>max:
        max=key
        
print(f"Length having maximum number of words is: {max}")

max_vowels=""
v_count_max=0

for ch in dict[max]:
    c=0
    for i in ch:
        if i.lower() in "aeiou":
            c+=1
    
    if c>v_count_max:
        v_count_max=c
        max_vowels=ch

        
    elif c==v_count_max:
        max_vowels=max_vowels+ " , "+ ch

print(f"The word(s) in the found length having maximum number of vowels is {max_vowels}")
s="python programming is easy"
#Output should be reverse of each word in sequence

l=s.split(" ")
print(l)
# l1=[]
# for ch in l:
# l1.append(ch[::-1])
# print(l1)
# rev=" ".join(l1)
# print(rev)

for ch in l:
    print(ch[::-1],end=" ") #Alternate method
s="python programming is easy"
#Output should be stored in a string and be reverse of each word in sequence

# l=s.split()
# str2=""
# for word in l:
# rev=word[::-1]
# str2=str2+rev+" "
# print(str2)

l=s.split()
l1=[]

for word in l:
    rev=word[::-1]
    l1.append(rev)
str2=(" ".join(l1))
print(str2)
#Find error in this  programme
str="programming"

dict={}
for i in str:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1

for key,value in dict.items():
    print(key,"->",value)

dict2=dict

for key,value in dict2.items():
    if value!=1:
        dict.pop(key)
print(dict)

a=20
b=a
a=10
print(a)
print(b)


str="programming"
#Remove duplicate characters with dictionary

dict={}
for i in str:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1

for key,value in dict.items():
    print(key,"->",value)

str2=''

for key in dict.keys():
    str2=str2+key
print(str2)
str="programming"
#Remove duplicate characters without dictionary

str1=""

for i in str:
    if i not in str1:
        str1=str1+i
print(str1)
str="programming"
#Remove duplicate characters using list

list=[]
for i in str:
    if i not in list:
        dict[i]=1
    else:
        dict[i]+=1

for key,value in dict.items():
    print(key,"->",value)

str2=''

for key in dict.keys():
    str2=str2+key
print(str2)
list=[1,2,3,4,5,3,3,22,33,6,7,8,9,10,12]
#Group using dictionary in even odd

dict={}
dict["Even"]=[]
dict["Odd"]=[]

for i in list:
    if i%2==0:
        dict["Even"].append(i)
    else:
        dict["Odd"].append(i)

for key,value in dict.items():
    print(key,"->",value)