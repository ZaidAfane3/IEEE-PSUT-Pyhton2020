x = 9 
# x++
x += 1   

x = x ** x  
x **= x

print (x)

######### 

y = 5  
print (isinstance(y, int))
y = str(y)
print (isinstance(y, int) , type(y))
y *= 2 
print (y)
y = int(y)
print (y*2)
exit (0)

x = input ("Please enter your age : ") 

gpa = float (input ("plz enter ur gpa: "))

print (gpa + 5 ) 

c = "Zaid"
x = 5 

###################

ahmad_age = int(input ("ahmed age : "))
zaid_age = int(input ("zaid age : "))


# # && => and 
# # || => or  
# # != 

if ahmad_age > zaid_age:
    print ("ahmad older than zaid :(")
    if zaid_age < 18 : 
        print ("batal Zaid")
    elif ahmad_age > 20:
        print ("Mr.Ahmed") 
elif ahmad_age < zaid_age:
        print ("ahmad younger than zaid :D")
        if zaid_age > 20 : 
            print ("Mr.Zaid")
        elif ahmad_age < 18:
            print ("bobo ahmed") 
else :
            print ("ahmad same as zaid :|")


######################### 

# for (int i = 0 ; i <10 ; i++){
# 
# }

# range(11) generates this (1,2,3,4,5,6,7,8,9,10)


for number in range(1,11): 
    print (number)
print (number)




i = 0
while (i < 11): 
    print (i)
    i+=1  






