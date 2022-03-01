# cars={'model':'mustad','brand':'ford','year':1989}
# print(cars['year'])
# print(type(cars))
# each key must be unique - it's not possible to have more than one key of the same value;
# a key may be any immutable type of object: it can be a number (integer or float), or even a string, but not a list;
# a dictionary is not a list - a list contains a set of numbered values, while a dictionary holds pairs of values;
# the len() function works for dictionaries, too - it returns the numbers of key-value elements in the dictionary;
# a dictionary is a one-way tool - if you have an English-French dictionary, you can look for French equivalents of English terms, but not vice versa.
# student={'department':'electrical','class:':'electrical engineering','yr':5}
# for key in student.keys():
#     print(key,'',student[key])
# cars={'model:':'mitsubishi','year':1889,'licenced' :'yes'}
# for key in cars.keys():
    # print(key,'=',cars[key])
# computer={'model':'bravia','year':1510,'owner':'student'}
# computer['model']='toshiba'
# computer['year']=2000
# computer.update({'faultiness':'no'}) 
# # you can add more characters in a dictionary
# # del computer['faultiness'] 'deleteing an item'
# for key in sorted (computer.keys()):
    
#     print(key,'=',computer[key])

# month_conversions={
# "jan":"janauary",
# "Feb":"february",
# "mar":"march"

# }
# print(month_conversions.get('ap','not valid'))
student=dict(name="gideon",age=90,street="newyork")
print(student) 
# keyss=student["name"]
# print(keyss)
# student["email"]="xyz@gmail.com"
# print(student)
# student.pop("name")
# print(student)
# print(len(student.keys()))
# try:
#    print(student["last name"])
# except:
#     print("error")
# for keys in student:
#     print(keys)
# for values in student:
#     print(keys,values)    
class2=student.copy()
print(class2)    
student["home"]="newyork"
student.pop("street")

print(student)
value=student["name"]
print(value)