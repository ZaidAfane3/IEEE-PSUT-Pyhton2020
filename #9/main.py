def some_function ():
    print ("Hello")
    return 5, "hello"


# => 5! => 120
# => 5 * 4!  => 5 * 24 
# =>     4 * 3!   => 4 * 6 
# =>          3 * 2!  => 3 * 2 = 6 
# =>              2 * 1! => 2*1 = 2
# =>                  1 * 1 

def factorial (a):
    if a == 1: 
        return 1 
    else:
        return a * factorial(a-1) 
print(factorial(5))

# signal 
#     copper for each 1 meter 3% 
#     fiber  for each 1 meter 0.5% 

#     a recursive function that takes signal strength and material 
#     and returns how many meters the signal will go till it become invalid (strength < 100)


def signal_meter (signal, material): 
    if signal <= 100:
        return 0 
    else: 
        if material == "copper":
            return 1 + signal_meter(signal - signal*0.03, material)
        if material == "fiber":
            return 1 + signal_meter(signal - signal*0.005, material)

print (signal_meter(1000,"fiber"))  


# => count of all number from 0 to 100 

def count (num):
    if num == 0:
        return 0 
    return num + count(num-1)


print(count(5))


# => power (a, b) -> a to the power b

def power(a,n):
    if n == 1:
        return a
    else:
        return a * power (a , n-1)

print (power(2,8))





