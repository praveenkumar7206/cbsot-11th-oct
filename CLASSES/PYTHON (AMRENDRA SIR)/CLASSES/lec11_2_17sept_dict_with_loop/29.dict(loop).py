# student_data={
#     "name":"aman",
#     "name":"sumit",
#     "name":"praveen",
#     "roll_num":2,
#     "add":"noida"
# }

# dictionary find
#print("add" in student_data)  if true the yes if false then no
# #only keys print
# print(student_data.keys())

# #onl;y value print
# print(student_data.values())

# # key and value print
# print(student_data.items())

# # for loop in dictionary
# for key in student_data:
#     print(key)

# for value in student_data.values():
#     print(value)

# for key,value in student_data.items():
#     print(f"{key}-{value}")



# cw
student={
    "python":80,
    "java":75,
    "c":40
}
student["HTML"]=60
print(student)
student["c"]=70
print(student)
del student["java"]
for key in student.keys():
    print(key)
for value in student.values():
    print(value)
for key,value in student.items():
    print(f"{key}--{value}")

student2={
    "phy":80,
    "chem":75,
    "math":40,
    "os":85,
    "java":98
}
sum=0
count = 0
less70=0
mmarks=0
msubj=""
lmarks=0

for key,val in student2.items():
    if val>80:
        print(f"u got 80+ in {key}")
    sum = sum+val
    count = count+1
    if val<70:
        less70=less70+1   
    if val>mmarks:
        mmarks=val
        msubj=key 
    if val<mmarks:
        lmarks=val
    

print(f"total marks are {sum}")
print(f"average marks are {sum/count}")
print(f"u got toal subject less than 70 {less70}")
print(f"max subjest is {msubj} have maxm mark{mmarks}")
print(f"have low mark{lmarks}")


