print("hello",end=" ")
print("world")
# if we want to print in same line use end command
# n= int(input("enter ur number for fibonaccci series"))

#1 methods
# a = 0
# b = 1
# c= 0
# for i in range(2,n+1):
#     i = a+b
#     c= i
#     a=b
#     b=c
#     print(i)

#2 method

# a = 0
# b = 1
# c= 0
# for i in range(n+1):
#     i = a+b
#     c= i
#     print(a,end=" ")
#     a=b
#     b=c

# 3rd method do using while loop

# n = int(input("enter ur number to check fibonacci number"))
# a = 0
# b = 1
# c= 0

# for i in range(n+1):
#     c = a+b
#     if c==n or a==n or b==n:
#         print("yes fibonacci number")
#         break
#     elif(c>n):
#         print("not a fibonacci")
#         break    
#     a=b
#     b=c



n = int(input("enter ur number to check fibonacci number"))
count = 0
a = 0
b = 1
c= 0
while(c<=n or c>n):
    c = a+b
    if c==n or a==n or b==n:
        print("yes fibonacci number")
        print(f"{count} is the place of that fibonacci number")
        break
    elif(c>n):
        print("not a fibonacci")
        break  

    a=b
    b=c
    count = count+1








