# x = 1 
# y = 1

# # & -> binary 
# print (x & y)

# # | -> or
# print (x | y)

# # ^ -> xor 
# print (x ^ y)

# # >> -> shift right 
# # 0001 >> 0000
# print (x >> 1)

# x = 7 # 0111
# y = 5 # 0101
#       # 0001

# print (x & y)

# print (y << 1)

# reg = 0xFA # 1111 1010 

# op = input("r or s")

# print (type(op))


# # 0100
# if op == "set":
#     print ("hello")
#     reg = reg | 0x04
# elif op == "reset":
#     pass

# print ('{0:08b}'.format(reg))
# print (bin(reg))


# names = ["zaid","ameen","omar"]
# print (len(names))

# for i in range (len(names)):
#     print (names[i])

# print (len("Zaid"))

# counter = 0 
# for i in "zaid":
#     counter+=1 

# print(counter)

names = []

# names[0] = "Zaid"
names.append("Zaid")
names.append("rinatta")
names.append(550)
names.append(3.3)
names.append([1,2,3])
#   ['Zaid', 'rinatta', 550, 3.3 , 1,2,3]
#   ['Zaid', 'rinatta', 550, 3.3 , [1,2,3]]

names.insert(3, 900)
#   ['Zaid', 'rinatta', 550, 900, 3.3 , [1,2,3]]
print (names)

# name = "zaid"
# name.append("a")
# print (name)
print (names[-1])

x = 5 
y = 9 


####
#temp = x
#x = y 
#y = temp 

x, y = y, x 
print (x , y) 



[1,2,3,4,5]
# rotate 
## fail - no method for lists 

# reverse 
names.reverse()
print (names)

# delete 
names.remove(900)
print (names)

del names[0]
print (names)

# split 
## fail - no method for lists 


# search
#in 

if 3.3 in names: 
    print (names.index("Zaid"))


# mirror 






