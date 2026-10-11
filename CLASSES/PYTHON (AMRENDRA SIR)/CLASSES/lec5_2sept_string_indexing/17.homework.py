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

# w = input("check ur word is palindrome or not")
# l = len(w)
# for i in range(l):
#         if w[i]==w[l-1-i]:
#             if i == l-1:
#                 print("a plaindrome")
#         else:
#             print("not a  palindrome")
#             break
                    
#ques 2
# w = input("check number of vowles and consonanats in word")
# w.lower()
# v = 0
# c = 0
# l = len(w)
# if w.isalpha()==True :
#     for i in range(l):
#         if w[i]=="a" or w[i]=="e" or w[i]=="i" or w[i]=="o" or w[i]=="u":  # or w[i] in "aeiouAEIOU"
#            v = v+1
#         else:
#             c = c+1
#     print(f"there are total {v} vowels and {c} consonants")        
# else:
#     print("invalid input , put only alphabet")            
            

#ques 3
# 3. take user input count frequency of each character in the given string (like how many charcter slike  a 2 1 n b) 
# w = (input("enter ur word"))
# wo=sorted(w)
# print(wo)
# for i in range (len(wo)):
#     print(f" {wo.count(wo[i])} are {wo[i]}")
#     x = int(wo.count(w[i])) 
#     i = i+x

# w = (input("enter ur word"))
w = "hwyegshdcg"
for i in w:
    print(f"freq of {i} is {w.count(i)}")






















 







    

    