# a = [3.3, 1, 3, "hello"]
# aa = [1,5,7,9,453,255,7,9,7]
# print (len(a))

# a.reverse()
# aa.sort()
# print (aa)

# names = ["zaid", "gaith", "khaled", "sara"]
# print (names[1:3])

list1 = [1,2,3,4]
list2 = [11,22,33,44]
list1 = list2 # 11,22,33,44
list2.append(55) # 11,22,33,44,55
list1.append(66)
print (list1 , list2)

# x = 5 
# y = 7 
# y = x # 5 
# x = 0 
# print (x, y) # 0 5 => 0 0  

# grades = [60,58,99,100,78,67,95,67,88,63,70,82]

# print (len(grades))
# backup_grades = grades[:len(grades)//2]
# grades.sort()
# print (grades)
# print (backup_grades)

name = "abcdefg"
# print (name[-1:])
# print (name[-2:])
# print (name[-1:-2])


# list [start index: end index: jumps (how many times i read before skip-1)]
print (name[:5:2]) # ace
print (name[:5:3]) # ad ,ab
print (name[:5:4]) # ae
print (name[:5:5]) # ae
print (name[1:5:5]) # ae

# https://docs.python.org/release/2.3.5/whatsnew/section-slices.html