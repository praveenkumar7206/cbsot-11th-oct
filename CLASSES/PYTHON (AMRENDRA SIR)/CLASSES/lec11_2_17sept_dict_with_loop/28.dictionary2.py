student_data={
    "name":"aman",
    "name":"sumit",
    "name":"praveen",
    "roll_num":2,
    "add":"noida"
}
print(student_data["name"])
# here last name prints because python works line by line , soo value of name updates each time that why praveen will be printed
print(student_data)

#only keys print
print(student_data.keys())

#onl;y val;ue print
print(student_data.values())

# key and va;ue print
print(student_data.items())

# get function
# print(student1_data["address"]) here using this way give error
print(student1_data.get("address","key is not available(we can write anything here)"))
# if that key is present , then it doesnt print our desired message
