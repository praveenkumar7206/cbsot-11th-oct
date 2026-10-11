#  greatest of 3 numbers as a input

# a = int(input("1st number"))
# b = int(input("2st number"))
# c = int(input("3st number"))
# if a>b and a>c:
#     print(a)
# elif b>c:
#     print(b)
# else:
#     print(c)    

# n = int(input("enter ur number"))
# if n%3==0 and n%5==0:
#     print("fizz buzz")
# elif n%3==0:
#     print("fizz")
# elif n%5==0:
#     print("buzz") 
# else:
#     print(n)   


# n = int(input("check ur number is prime or not ?"))
# c = 0
# for i in range (2,n):
#     # we can also runn from 2 to till n//2 soo for more optimization we can loop from 2 to square root of n like(int(n**0.5)+1) 
#     if n%i==0:
#         c=c+1
#         break
# if c==0:
#     print("prime")
# else:
#     print("not prime")

n = int(input("check ur number is prime or not ?"))
c = 0
for i in range (2,int(n**0.5)16+1):
    # we can also runn from 2 to till n//2 soo for more optimization we can loop from 2 to square root of n like(int(n**0.5)+1) 
    if n%i==0:
        c=c+1
        break
if c==0:
    print("prime")
else:
    print("not prime")
