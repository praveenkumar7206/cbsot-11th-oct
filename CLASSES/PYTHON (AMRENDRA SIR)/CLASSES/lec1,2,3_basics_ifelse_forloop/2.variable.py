# a=10
# _a29745279hjrfgh=10
# print(type(_a29745279hjrfgh))
# _a="hello"
# k  =23890
# print(k)

# print(id(a))
# a =9
# b =a
# print(id(a))
# print(id(b))
# print(a==b)
# print(a is b)

a= 12
b =12
c =12
d = 12
e =12
print(id(a))
print(id(b))
print(id(c ))
print(id(d ))
print(id(e ))
print(a==b)
print(a is b)
# kabhi same integer alag alag variable ko assign karenge too sada variable , 12 ka hi ref address store karta hai , sabka lia alag alag memory nhi banta

# soo conlcusion ye hai ki agar data type same hai and data same hai too sabko same hi address milega

# a= 12
# b = "12"
# print(id(a))
# print(id(b))
# print(a==b)
# print(a is b)
# print(" a is " ,a, "b is" ,b, "hello world" , "cbsot" )

a= 12
b = "12"

print(id(a))
print(id(b))
print(type(a))
print(type(b))
b = int(b)
print(type(b))
print(a==int(b))

b = 12.4
print(type(b))
b= str(b)
print(type(b))
print(b)






