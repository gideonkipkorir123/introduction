# numbers = []
# for x in range [5]:
#     print(numbers)

# # print("List content:", numbers)  # Printing original list content.
# # numbers.append(4) #adds at the end of a list
# # print(numbers)
# # numbers.insert(1, 3) #specific position
# # print(numbers)
# # print(numbers[3])
# # print(len(numbers)) #Returns the number of elements
# # print(numbers[1:]) # prints elements from the specified index
# # print(numbers[1:3])
# # print(numbers[:3]) #prints numbers to a specified index
# # print(numbers[:]) #prints the entire list
# # print(numbers[-1])  #prints the last element of a list
# # print(numbers[len(numbers)//2]) #to print the middle element in a list
# # print(numbers[::-1]) #To reverse a list

# list1 = [1,2,4,3,5,6,7]
# # list1.reverse()
# # print(list1)
# list2 = []
# list3 = []
# list4=[]
# for x in list1:
#     if x%2 !=0:
#         list4.append(x)
# print(list4)    
# for i in list1:
#     if i%2 == 0:
#         list2.append(i)
#     else:
#         list3.append(i)
# # print(list1)
# print(list2)
# print(list3)        


# list2.extend(list3)
# print(list2)
# print(list3)
# # list1.sort()
# # list1.reverse()
# # # print(sorted(list1))
# # print('sorted list',list1)

# # # tuples are immutable that means they cannot be appended
# # # tuple1 = (1,2,4,3,6,5,7) # This is a tuple
# # # tuple2 = (4,)
# # # print('Tuple1: ',tuple1)

# # # tuple=(1,2,3,4,5,6,7,8,9)
# # # tuple2=(0,345)
# # # print(tuple,tuple2)
# # # pop actually removes ther last item in a list
# # student=['mike','silvia','kimaiyo']
# # student.pop()
# # print(student)
# # print(student.index('mike'))
# # print(student.count('mike'))
# # student2=student.copy()
# # print(student2)
# # print(len(student2))
# # step index
# list5=[1,2,3,4,5,6,7,8,9,9,3,3,3,3,3]
# # print(list5[1::2])
# # print(list5[::-1])
# # (list5.reverse())
# # print(list5)
# b= [x*x for  x in list5]
# print(b)
# count=list5.count(3)
# print(count)

students=(1,2,3,4,5,5,55,4,5)
# print(students.count(5)
# )
# print(students.index(55)
# )
list6=list(students)
print(list6)
students2=[1,2,3,4,5,6,7,8,9]
tuple=tuple(students2)
print(tuple)
my_tuple=(0,1,2,3,45,34)
i1,i2,i3,*i4=my_tuple
print(i1)
print(i2)
print(i3)
print(i4)
