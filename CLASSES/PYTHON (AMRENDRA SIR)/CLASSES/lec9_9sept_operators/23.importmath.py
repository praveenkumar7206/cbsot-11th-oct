import math
max=-math.inf

n= int(input("how many numbers u want to compare?"))
for i in range (1,n+1):
    i=int(input(f"enter ur {i} number"))
    nx=i
    if nx>=max :
        max=nx
print(max)



# also try without importing - infinity  


#     if nx<=big:
#         ny = nx
#         if ny>small:
#            small=nx

# if big>0 :
#      if big>small :
#          print(big)   
# if big<0:
#     if big>small:
#         print(big)
#     else:
#         print(small)                 
# if big==0:
#     print(small)