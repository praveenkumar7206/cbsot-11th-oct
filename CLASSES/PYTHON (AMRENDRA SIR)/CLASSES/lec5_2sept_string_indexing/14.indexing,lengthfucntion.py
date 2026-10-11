s = "python"
for i in range (0,6):
    print(s[i])
    # +ve indexing]
    # -ve indexing
name = "praveen"
for i in range (len(name)):
    print(name[i])

for i in name: # here if we write i in name , we r not going on index this time but it will actuaslly go to value of index , like he first go to 0 but it access the chaarcter ya value on that a  index , soo becuase of this we directly write print(i) not print(name[i])
    # so this is the main diff between i in range and i in name 

    # always do it like i in range 
    
    print(type(i)) 
    print(i)


# length fucntion
s= "kumar"
print(len(s))  #5

s = 'ram kumar'
print(len(s))  # 9 becuase space is also a character
















