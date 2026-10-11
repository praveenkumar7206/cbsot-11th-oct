# string multiply and print horizontally
# s = "hi"
# print(4*s)

# #concatination(add two string and u can insert space also AND MANY THINGS)
# f_name="praveen"
# l_name= "kumar"
# name = f_name+" "+l_name
# print(name)


# # charcter checking
# s = "python"
# print("P" in s ) # false becuase capital p is not in python becuase in pyhton small and capital have differnt value 
# print("x"  not in s ) # true becuase x is not in s 

# # convert in small and capital letter
# s1 = "Hello World"
# print(s1.lower())
# print(s1.upper())

# #find() # here find , finding exact  python in ur string and gives u index value where it starts from , it finds from right to left soo first come first server basis will give index , if it didnt able to find it exact same then it will give -1
# str = "hello python"
# print(str.find("python"))
# print(str.find("Python"))
# print(str.find("thon"))
# print(str.find(" "))
# # print(s[1:1jjjjjjjjjjjjjjpwavee n kumar'}}}ppwpwweffn jiojaiojflkg  k'jiju] 'pjo==poav=v====prhjkl'])
# # n = "12345"
# # sum = 0
# # for i in range (5):
# #     x = n[i]
# #     x=int(n[i])
# #     sum = sum + x
# # print(sum) 
# # 
# #    
# # n = int(input(ur number))
# # while n >0:
# #     sum =/10
# # print(sum)  sum + n%10
# #     n = n/  


# n = 1234
# sum = 0
# for


# n = int(input("ur number")) # do by 2 method on last digit or ya whole number n
# sum = 0
# while n >0:

#     if n%2!=0:
#         sum = sum + n%10
#     n = n//10

# print(sum)
    
# n = int(input("ur number"))
# m = 1
# o=0
# while n>0:
#     if n%10==0:
#         n=n//10
#             continue
        
#     else:
#         a = n%10
#         m = m*a
#     n = n//10
# print(m) 

# int=123
# rev = 0
# while int>0:
#     rem = int%10
#     rev = rev*10+rem
#     int=int//10
# print(rev)   

# 1. take user input and check whether the user input is palndrome or not? for number and string both
# 2. take user input and count vowwl of a string and also consonant
# 3. take user input count frequency of each character in the given string (like how many charcter slike  a 2 1 n b) 
# 4. check whether 2 strings are anagram
#(hint for 4 and 4 use sorting then equate)
# 5. do all questions using for loop by taking input as integer not as string
# 6. reverse any number without converting tha number to string like 123 to convert 321 . 

#ques1 part 1.
# n = int(input("check ur number is palindrome or not"))
# int = n
# pal=0
# while n>0:
#     pal = pal*10+ n%10
#     n = n//10
# print(pal)    

# if pal==int:
#     print("palindrome")
# else:
#     print("not a palindrome")

#ques 1 part 2
w = input("check ur word is palindrome or not")
l = len(w)
for i in range(l):
        if w[i]==w[l-1-i]:
            if i == l-1:
                print("a plaindrome")
        else:
            print("not a  palindrome")
            break
                    
            



















 






