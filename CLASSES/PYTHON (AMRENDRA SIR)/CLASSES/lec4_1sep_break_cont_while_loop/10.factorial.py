#take user input a number and find factorial number 
no = int(input("enter ur number"))
f = 1
for i in range(1,no+1,1):
    f = f*i
print(f)    


no = int(input("enter ur number"))
f = 1
a = 1
while a<=no:
    f=f*a
    a = a+1
print(f)    
