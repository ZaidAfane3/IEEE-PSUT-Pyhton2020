# Task 1 
#num = int(input("Please enter a number"))

#print (num>=100)




# Task2 

grades = []
max = 0 
min = 101
i = 0 
sum = 0 
avg = 0.0

while i < 5 : 
    grade = int(input("please enter your grade: "))
    grades.append(grade)
    
    # MAX AND MIN 
    if grade > max: 
        max = grade 
    if grade < min and grade >= 0: 
        min = grade 
    
    # Sum for average  
    sum += grade 

    i+=1 

avg = sum/5

i = 1
for grade in grades:
    if (grade > 90 and grade <= 100):
        print ("Student number %d GOT A"%(i))
    elif (grade > 80):
        print ("Student number %d GOT B"%(i))
    elif (grade > 70):
        print ("Student number %d GOT C"%(i))
    elif (grade > 60):
        print ("Student number %d GOT D"%(i))
    else:
        print ("Student number %d GOT F"%(i))
    i+=1 



print ("""
        highest grade is %d,
        lowest grade is %d,
        the average is %0.2f,
"""%(max,min,avg))




     
