# largest_number = -99999999
# counter = 0

# while True:
#     number = int(input("Enter a number or type -1 to end program: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number

# if counter != 0:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")
# smallest_number=1000
# counter=0
# while True:
#     number=int(input('enter number to be run'))
#     if number==-1:
#         break
#     counter+=1
#     if number > smallest_number :
#         smallest_number=number
#     if counter !=0:
#         print('the largest number is:',smallest_number) 
#     else:
#         print('please enter a valid number')

largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")



