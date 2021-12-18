# my_list = [8, 10, 6, 2, 4]  # list to sort
# swapped = True  # It's a little fake, we need it to enter the while loop.

# while swapped:
#     swapped = False  # no swaps so far
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # a swap occurred!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)
b = 2

a,b = b,a
print('a: ',a)
print('b: ',b)

list = []
for i in range(1,6):
    list.append(i)
print(list)
list[1],list[2] = list[2],list[1]
print('New list: ', list)

list2 = ['Bilo','Tony','Mercy','Grace','Ngatia']
list2.append('Dennis')
print(list2)
