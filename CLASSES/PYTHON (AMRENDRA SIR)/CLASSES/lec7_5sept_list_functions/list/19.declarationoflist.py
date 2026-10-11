# declaration of list
# 3 list can multiple data type data i n vairable of list
roll=[1,2,3,4]
print(roll)
name=["abc","ram","shyam",1,"pythgon"]
print(name)
name[0]="abcde"
print(name)
data =[1,1.5,"abc",'a',"cbsot"]
print(data)

for i in name:
    print(i)

list=[]
list.append("python")
list.append(1)
# using append function we can add any data to list using this function
# append add any thing to variable to add in last place
print(list)
# +ve and-ve indexing is also in list
print(list[1])
print(name[-5])
count=1
for i in name:
    print(f"{count}-{i}")
    count=count+1
print(name[:])
print(name[-1:-6:-1])
print(name[4:0:-1])
print(name[4:1:-1])












