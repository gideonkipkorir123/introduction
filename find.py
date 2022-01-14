# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# found = False

# for i in range(len(my_list)):
#     found = my_list[i] == to_find
#     if found:
#         break

# if found:
#     print("Element found at index", i)
# else:
#     print("absent")
list=[1,2,3,4,5,6,7,8,9,10]
to_find=6
found=False
for x in range(1,len(list)):
    found=list[x]==to_find
    if found:
        print('located at point: ',x)
    else:
        print('element not found')


