s = "praveen"
print(s[:])
print(s[:7])
print(s[1:7:2])
print(s[-1:-5:-1]) # here we use - 1 becuase we want to - 1 to move back ward l;ike - 1, -2 , -3 till - 4 , soo it will print word acc to negative indexing  
print(s[::-1])  #here after giving - 1 , it goes back ward like 0 then - 1then -2 acc to negative indexing it will print the word reverse in order 
#[x:y:z] z is step value , how many steps u want to jump

# immutable function (we cannot chnage the index value of string but if u wan to do it u need reassign the value of string that u want to change )
s = "python"
s[1]=='t'
print(s)

s = "python"
print(s[-3:-6:-1])

s = "python"
s1= "j" + s[1:]
print(s1)

s2 = s[:2]+"x"+s[3:]
print(s2)

# we dont directly put value like s = jython ya pyxthon becuase i9f we do like that we make new memory address , old ref of actual python will be vansihed , soo because of that we do like that , so we can have reference of orginal s = "python"





 