# # anagram
# # n1 = "silent"
# # n2 = "silent"
# # c = 0
# # for ch in n1:
# #     n1.count(ch)!=n2.count(ch)
# #     c= c+1
# #     print("not anagram")
# #     break

# # if c==0:
# #     print("anagram")

# # s = "programming"
# # freq={

# # }

# # for ch in s:
# #     if ch in freq:
# #         freq[ch]=freq[ch]+1
# #     else:
# #         freq[ch]=1
# # print(freq)

# n1 = "silent"
# n2 = "entsil"

# freq1={}
# freq2={}
# if len(n1)!=len(n2):
#     print("not anagram")
# else:
#     for ch in n1:
#         if ch in freq1:
#             freq1[ch]=freq1[ch]+1
#         else:
#             freq1[ch]=1

#     for ch in n2:
#         if ch in freq2:
#             freq2[ch]=freq2[ch]+1
#         else:
#             freq2[ch]=1
#     if freq1==freq2:
#         print("anagram")
#     else:
#         print("not a anagram")
#  # dictionary does not  follow order    

# do without making 2 dictionary make only one dictionary

#  # print most frequent character and least freq, 

m= "programming in python python is easy cbsot gla"
m=m.replace(" ","")
freq={}
for ch in m:
    if ch in freq:
     freq[ch]=freq[ch]+1
    else:
        freq[ch]=1
print(freq)
max=0
mchr=""
lchr=""
low=0
for key,val in freq.items():
    if val>max:
      max=val
      mchr=key
    if val<max:
      low=val
      lchr=key  

print(f"max is {mchr}")
print(f"low is {lchr}")

# which character is non reperatinga nd first uin order
