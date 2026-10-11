# DICTIONARY
student_data={
    1:"vishnu",
    2:"sumit",
    3:"praveen",
    "name1":"name",

}
print(student_data[1])
print(student_data[2])
print(student_data[3])
print(student_data["name1"])
student1_data={
    "name":"praveen_kumar",
    "age":20,
    "mobile_number":9772516035,
    "is_depressed":True ,
    1:1,
    "1":2,
    "roll_num":[1,2,3,4,5]
    # in storing variable in decitionary we use double quote
    
}
print(student1_data)
print(student1_data["name"])
print(student1_data["age"])
print(student1_data["is_depressed"])


# nested loop (discyionary in dictionary)
# A nested dictionary storing employee data
employees = {
    "emp1": {
        "name": "Alice", 
        "role": "Developer", 
        "salary": 85000
    },
    "emp2": {
        "name": "Bob", 
        "role": "Designer", 
        "salary": 70000,
        2:2,
    }
    # 3:{
    #     "name":"sumit"
    # }
}
print(employees.items())
# print(employees["emp2"][2])
# print(employees)
# employees["emp1"]=["emp0"]
# employees["emp1"]["salary"]=80000
# print(employees)

student1_data={
    "name":"praveen_kumar",
    "age":20,
    "mobile_number":9772516035,
    "is_depressed":True ,
    1:1,
    "1":2,
    "roll_num":[1,2,3,4,5]
}
# if they cannot able to find any ket just for example city key , if not found it will add to data and if key matches it will update thatvalue
student1_data["city"]="noida"
student1_data["age"]=22
print(student1_data)

# key delete
del student1_data["1"]
print(student1_data)
#pop
student1_data.pop(1)
print(student1_data)

# # clear data of  whole targeted dictionary
# student1_data.clear()
# print(student1_data)

# print all the keys
print(student1_data.keys())
# ye important , hai kyu ki ham loop ispa hi lagayenge.


# print all the values
print(student1_data.values())

# print key with value
print(student1_data.items())

# get function
# print(student1_data["address"]) here using this way guive error
print(student1_data.get("address","key is not available(we can write anything here)"))
# if that key is present , then it doesnt print our desired message

# for loop
for key in student1_data:
    print(key,student1_data[key])