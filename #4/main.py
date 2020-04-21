##### iteratable Data Types #### 

name = "Zaid"
array = [1,2,3,4] # mutable 
tup = (1,2,3,4) # immutable 
dictionary = {"name":"zaid" , "age":21}

# immutable 
# mutable 

for i in name: 
    print (i)

for i in array: 
    print (i)

for i in tup: 
    print (i)

for i in dictionary: 
    print (i)


##### Lists ####

print (array) 
print (type(array))

name = ["zaid", "ahmed", "khaled"]
print (name) 
print (type(name))

grades = [98.2,84.3,66.5]
print (grades) 
print (type(grades))

no_dt_list = ["name", 10 , 1.6, [1,2,"zaid"]]
print (no_dt_list[3][2])

list_unkown = [
    [1,2,3],
    [1,2,3],
    [1,2,3,4],
]
print (list_unkown)

print (no_dt_list) 
print (type(no_dt_list))


import socket 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


data = [1,6.5,"zaid",0x55,server,'psut', [1,2,3 , [5,6,7]]]

str_count = 0 # 2
int_count = 0 # 2
float_count = 0 # 1 
idk_count = 0 # 2
list_count = 0 # 

name = 5 
name = "zaid"

for member in data:
    if isinstance(member,int):
        int_count+=1 
        print ("[*] int found =>", member)
    elif isinstance(member,str):
        str_count+=1
        print ("[*] str found =>", member)
    elif isinstance(member,float):
        float_count+=1
        print ("[*] float found =>", member)
    elif isinstance(member,list):
        list_count += 1 
        print ("[*] list found =>")
        # for i in range(3):
        #     print (member[i], end="\t")
        for i in member:
            if isinstance(i,list):
                list_count+=1
                print (">found a nested list<", end="\t")
                continue 
            print(i, end="\t")
        print()
    else:
        idk_count+=1 
        print ("[!] Unkown Data Type found of " , type(member))

# # 1- not gonna work 5
# # 2- work partially 4 :D
# # 3- works fine 4

print(int_count,str_count,float_count, list_count, idk_count, sep="\n")
server.close()

# (0,1,2,3,4,5,6,7,8,9)

for i in range (10):
    if (i == 5): 
        continue
    print(i)

# 0,1,2,3,4,6,7,8,9

sum = 0 
count = 0 
while True:
    grade = int(input("Please enter a grade: "))
    if (grade < 0):
        break
    sum += grade 
    count += 1

# this correct too
# print ("sum = {0}\ncount = {1}\navg = {2}".format(sum, count, sum/count))

print ("sum = %d\ncount = %d\navg = %0.2f" %(sum,count,sum/count))

#this is wrong 
#print ("sum = \n",sum,"count = \n",count,"avg = ", sum/count) 

print ("THE END")




























