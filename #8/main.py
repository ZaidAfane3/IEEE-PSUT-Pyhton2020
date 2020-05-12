# list1 = [1,1.5,2,3,4]

# tuple1 = (1,2,3,4)

# grades_second2020 = (0.50 , 0.50)
# grades_summer2020 = (0.25, 0.25 , 0.10, 0.40)
# pi = (3.14)
# addr = ("10.10.10.1" , 8080)

############################# 
# Dictionary => {Key: Value}
# name_dict = {
#     "Zaid":{
#         "Age": 21,
#         "Phone Number": "079000000",
#         "Email": "afaneh.zaid98@gmal.com"
#     },
#     "Ameen":{
#         "Age": 22,
#         "Phone Number": "079000000",
#         "Email": "skjhgkjshg@gmal.com"
#     },
#     "Nader":{
#         "Age": 21,
#         "Phone Number": "079000000",
#         "Email": "gdgjsldkjgf@gmal.com"
#     },
#   }

# # print(name_dict["Ameen"])

# name_dict ["Ahmad Alkhatib"] = "MR.Transistor"
# print(name_dict["Ahmad Alkhatib"])

# print (name_dict["Zaid"])
# print (name_dict["Zaid"]["Age"])

# prayer = {
#    "code": 200,
#    "status": "OK",
#    "data": [{
#        "timings": {
#            "Fajr": "03:57",
#            "Sunrise": "05:46",
#            "Dhuhr": "12:59",
#            "Asr": "16:55",
#            "Sunset": "20:12",
#            "Maghrib": "20:12",
#            "Isha": "22:02",
#            "Imsak": "03:47",
#            "Midnight": "00:59"
#        },
#        "date": {
#            "readable": "24 Apr 2014",
#            "timestamp": "1398332113",
#            "gregorian": {
#                "date": "15-05-2018",
#                "format": "DD-MM-YYYY",
#                "day": "15",
#                "weekday": {
#                    "en": "Tuesday"
#                },
#                "month": {
#                    "number": 5,
#                    "en": "May",
#                },
#                "year": "2018",
#                "designation": {
#                    "abbreviated": "AD",
#                    "expanded": "Anno Domini",
#                },
#            },
#            "hijri": {
#                "date": "01-09-1439",
#                "format": "DD-MM-YYYY",
#                "day": "01",
#                "weekday": {
#                    "en": "Al Thalaata",
#                    "ar": "الثلاثاء",
#                },
#                "month": {
#                    "number": 9,
#                    "en": "Ramaḍān",
#                    "ar": "رَمَضان",
#                },
#                "year": "1439",
#                "designation": {
#                    "abbreviated": "AH",
#                    "expanded": "Anno Hegirae",
#                },
#                "holidays": [
#                    "1st Day of Ramadan"
#                ],
#            },
#        },
#        "meta": {
#            "latitude": 51.508515,
#            "longitude": -0.1254872,
#            "timezone": "Europe/London",
#            "method": {
#                "id": 2,
#                "name": "Islamic Society of North America (ISNA)",
#                "params": {
#                    "Fajr": 15,
#                    "Isha": 15
#                }
#            },
#            "latitudeAdjustmentMethod": "ANGLE_BASED",
#            "midnightMode": "STANDARD",
#            "school": "STANDARD",
#            "offset": {
#                "Imsak": 0,
#                "Fajr": 0,
#                "Sunrise": 0,
#                "Dhuhr": 0,
#                "Asr": 0,
#                "Maghrib": 0,
#                "Sunset": 0,
#                "Isha": 0,
#                "Midnight": 0
#             }
#         }
#     },
#     {
#        "timings": {
#            "Fajr": "03:57",
#            "Sunrise": "05:46",
#            "Dhuhr": "12:59",
#            "Asr": "16:55",
#            "Sunset": "20:12",
#            "Maghrib": "20:12",
#            "Isha": "22:02",
#            "Imsak": "03:47",
#            "Midnight": "00:59"
#        },
#        "date": {
#            "readable": "24 Apr 2014",
#            "timestamp": "1398332113",
#            "gregorian": {
#                "date": "15-05-2018",
#                "format": "DD-MM-YYYY",
#                "day": "15",
#                "weekday": {
#                    "en": "Tuesday"
#                },
#                "month": {
#                    "number": 5,
#                    "en": "May",
#                },
#                "year": "2018",
#                "designation": {
#                    "abbreviated": "AD",
#                    "expanded": "Anno Domini",
#                },
#            },
#            "hijri": {
#                "date": "01-09-1439",
#                "format": "DD-MM-YYYY",
#                "day": "01",
#                "weekday": {
#                    "en": "Al Thalaata",
#                    "ar": "الثلاثاء",
#                },
#                "month": {
#                    "number": 9,
#                    "en": "Ramaḍān",
#                    "ar": "رَمَضان",
#                },
#                "year": "1439",
#                "designation": {
#                    "abbreviated": "AH",
#                    "expanded": "Anno Hegirae",
#                },
#                "holidays": [
#                    "1st Day of Ramadan"
#                ],
#            },
#        },
#        "meta": {
#            "latitude": 51.508515,
#            "longitude": -0.1254872,
#            "timezone": "Europe/London",
#            "method": {
#                "id": 2,
#                "name": "Islamic Society of North America (ISNA)",
#                "params": {
#                    "Fajr": 15,
#                    "Isha": 15
#                }
#            },
#            "latitudeAdjustmentMethod": "ANGLE_BASED",
#            "midnightMode": "STANDARD",
#            "school": "STANDARD",
#            "offset": {
#                "Imsak": 0,
#                "Fajr": 0,
#                "Sunrise": 0,
#                "Dhuhr": 0,
#                "Asr": 0,
#                "Maghrib": 0,
#                "Sunset": 0,
#                "Isha": 0,
#                "Midnight": 0
#             }
#         }
#     }
#     ]
# }
# print (type(prayer["data"]))
# # print (prayer)
# date = prayer ["data"][0]["date"]["readable"]
# print ("prayer times for %s"%(date))
# timings = prayer["data"][0]["timings"]
# for i in prayer["data"][0]["timings"]:
#     print("the time of ", i ,"prayer is =>", timings[i])

# # print (prayer["data"][0]["timings"]["Maghrib"])

# import requests
# import ast
# req_api = "https://api.nasa.gov/planetary/apod?api_key=zechg5by7rPOgb0UrVSaWJbPUzlCayy8XxR31Gzf"
# response = requests.get(req_api)
# print (type(response))
# print (response.status_code)
# # print (response.content)
# content = response.content
# print (content)


# def [name of the function] (arg1, arg2, arg3, ....) :
    # body of the function 


def print_list (a):
    print ("The Content of the list is:")
    for i in a: 
        print (i)
    print ("########################")

def sum (a, b):
    return a+b 



def calculate_gardes_info(list1):
    max = -1
    min = 10000
    sum = 0 
    for i in list1:
        if (i > max):
            max = i
        elif (i < min):
            min = i
        sum+= i 
    avg = sum/len(list1)

    return min, max, avg



def calculate_gardes_info_list (list1):
    max = -1
    min = 10000
    sum = 0 
    for i in list1:
        if (i > max):
            max = i
        elif (i < min):
            min = i
        sum+= i 
    avg = sum/len(list1)

    list_data = [min, max, avg]
    return list_data



def calculate_gardes_info_tuple (list1):
    max = -1
    min = 10000
    sum = 0 
    for i in list1:
        if (i > max):
            max = i
        elif (i < min):
            min = i
        sum+= i 
    avg = sum/len(list1)

    tuple_data = (min, max, avg)
    return tuple_data

def calculate_gardes_info_dict (list1):
    max = -1
    min = 10000
    sum = 0 
    for i in list1:
        if (i > max):
            max = i
        elif (i < min):
            min = i
        sum+= i 
    avg = sum/len(list1)

    dict_data = {
        "max": max,
        "min": min,
        "avg": avg,
    }
    return dict_data



# list1 = ["Zaid", "Nadeem", "Nader", "Ameen"]
# print (list1) 
# print_list(list1)

print (sum (5,10))


grades = [10,6,5.5,8,10,2]
print (calculate_gardes_info_list(grades))
print (calculate_gardes_info_tuple(grades))
print (calculate_gardes_info_dict(grades))
info = calculate_gardes_info_dict(grades)

for i in info:
    print (i , info[i])



print (calculate_gardes_info(grades))
#print (type(calculate_gardes_info(grades)))


min1, max1, avg1 = calculate_gardes_info(grades)
print (min1, max1, avg1)



