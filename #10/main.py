




# try :
#     x = int(input("enter a number: "))
#     y = int(input("enter a number: "))
# except:
#     print ("keyboard interrupt ?")
#     # close connection 
#     exit (0)


# ## open connection to server 


# # ZeroDivisionError: division by zero
# try : 
#     print (x/y)
# except:
#     while x == 0 or y == 0:
#         print ("one of the inputs is zero, please re-enter the number ")
#         x = int(input("enter a number: "))
#         y = int(input("enter a number: "))
#         print (x/y)




# # ModuleNotFoundError: No module named 'math1'
# # try : 
# #     r = int (input("please enter the radius: "))
# #     import math1
# #     print (pow(r,2) * math1.pi)
# # except:
# #         print (pow(r,2) * 3.14)




# names = ["zaid" , "omar" , "cathrine"]
# ## 
# ## 
# ## 
# ## 
# ## 

# try: 
#     x = -10
#     print (names[x])
# except:
#     print ("index error, the value of the index variable is " , x)
#     ## close connection 







# print ("Hello to our site ")
# ## close connection to server 
import sys 

# Segmentation fault: 11

try : 
    import sys 
    def fact (x): 
        if x < 1 :
            raise BaseException ("Factorial cannot be calculated for Zero")
        if x == 1:
            return 1 
        return fact(x-1) * x 

    num = int (input("plz enter a number: "))
    print (fact(num))

except KeyboardInterrupt:
    exit (0)
except RecursionError:
    import sys
    sys.setrecursionlimit(num+100)
    print (fact(num))
except NameError: 
    print ("GO LEARN PYHTON VAR !!! ")
    exit(1)
except BaseException as err:
    print ("Error Occured: " , err)
    exit (1)


