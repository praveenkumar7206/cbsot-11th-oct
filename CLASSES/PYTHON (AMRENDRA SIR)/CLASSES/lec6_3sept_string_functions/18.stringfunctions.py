# str = input(" enter ur name")

# rev = str[::-1]
# print(id(str)) # here both id will be different because any fucntion send string , then it will be saved in new address
# print(id(rev))
# if str==rev:
#     print("palindrome")
# else:
#     print("not a palindrome")    


name = "praveen"
print(f"your name is {name.upper()}")

# all are fucntions , if we pass any values to functions that is called arguments
# check all are alphabets ya number or not ?
str = "abc"
print(str.isalpha()) # here we are saying all char in str are alphabet or not ?
print(str.islower()) # here we can check that all alphabet are lower and upper
print(str.isupper())
s = "123"
print(s.isnumeric())  # here we are saying all char in str are numberic or not ?
p = "abc123"
print(p.isalnum()) # here we can check that both alphabet and numeric are available or not ?
s="dgcabch  wab cowqe    iydqvabchac"
print(s.count("a")) # using this fucntion we can count that how many character ya sub string is in that string .
print(s.count("abc"))


w = input("enter ur word")
l = len(w)
rev=""
while l>=0:
    rev =rev+ w[l-1]
    l=l-1
print(rev)


# str = "abcd"
# s=""

# for ch in str:
#     s = ch +s
# print(s)    
     

# replace function
str = "python language is very easy"
str = str.replace(" ","_") # sabsa first ma dalna hai kya replace karna ha and last ma kisse replace karna hai
print(str)
str = str.replace("pyth","_")
print(str)












     