# print odd number in given range
for i in range(10):
    if i%2!=0:
        print(i)

# without modulous using

for e in range(10):
     if e%2==0:
         break  #yaha e 0 se start hogqa and 0%5 o hi hota hai, sooo agar koi loop ma break active hogaya
     #suu uska baad ka kuch bhi loop nhi chalega doesnt matter uskA BAAD KITNA LOOP HAI USS FOR KE ANDAR JISKA ANDAR BREAK HAI
print(e)


for i in range(1,10):
    for j in range(1,10):
        if j%5==0:
            break
        elif j%2==0:
            print(j)
    print(i)        



for i in range (10):
    if i%2==0:
        continue # jasa uska upar wala statement true hoga then wo nicha wala sabkuch skip kar dega especially uss time y avlue par jo statement true hua hai , skip sirf apna just parent wala for ya while loop ke andar ke chizo ko skip karega jo continue ke baad aagaye and wapas se for and while loop chlaega 
    
    print(i)
    print(f"hello {i}")










