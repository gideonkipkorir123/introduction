# car={'mustard','toyota','bmw'}
# print(len(car))
# print(type(car))
# set ={1,2,3,4,5,55,5,5,5}
# print(set)
# unordered,mutable data that doesnt allow duplicate data
student=set()
# x=set(student)
# print(x)
# classx=set("hello")
# print(classx)
student.add(8)
student.add(9)
student.add(100)
student.remove(8)
student.discard(8)
print(type(student))
if 9 in student:
    print ("yes")
else:
    print("no")    
print(student)

for x in student:
    print(x)