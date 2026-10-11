for i in range (1,6):
    print(f"{i} hello world")

for value in range (100,100):
    print(value) 


       
odd = 0
even = 0
for ram in range(1,101):

    if ram%2==0:
        print(f"{ram} is even")
        even = even+1
    else : 
        print(f"{ram} is odd") 
        odd = odd+1 
print(f"{odd} odd") 
print(f"{even} even")  


items = ('milk' , 'bread' , 'lassi' , 'fruits')
count = 1
for item in items :
    print(count ,"buying", item )
    count+=1

