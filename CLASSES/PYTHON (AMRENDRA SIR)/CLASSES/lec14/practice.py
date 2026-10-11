# overall maxm for consecutive same digitts
# list = [1,1,0,0,0,1,0,0,1,0,0,0,0,0,1]
# max = 0 
# c = 0
# co=0
# for i in list:
#     if (i==0):
#         c = c+1 
#     else :
#         co =c 
#         c=0
#         if (co>max):
#             max = co
            
# print(max)


# list = [1,1,0,3,0,0,1,5,0,1,7,0,0,0,0,1,0] # int his question , we ca do negative indexing remove but cannot do +ve indexing remove , becuase it wioll shift loop will not run properly
# c = 0
# for i in list :
#     if (i==0):
#         c= c+1
# for j in range (c):
#     list.remove(0)
#     list.append(0)
# print(list)

# list = [1,2,1,2,1,2,3,4,5,4,4,1,6,1]
# # find highest freq no.
# dict =  {}
# for i in list :
#     if i in dict :
#         dict[i]= dict[i]+1
#     else :
#         dict[i]=1
# print(dict)
# max = 0
# k = 0
# max2 = 0
# k2 = 0
# for key,value in dict.items() :
#     if value >max:
#         max = value
#         k = key
#     if value<max  :
#         if value>=max2 and key>k2:
#             max2=value
#             k2 = key
            
# print(k)
# print(k2)

l = [4,1,2,3,6,5,8,4]
tar = 7
pair = 0
for i in l:
    for j in l:
        if i+j==7 :
            pair = pair +1
if pair>0:
    print("true")
else:
    print("false")
print(pair/2)

# list=[4,2,1,6,9]
# for i in range(len(list)):
#     for j in range (i+1 , len(list)):
                 
        