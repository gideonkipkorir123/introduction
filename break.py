# # break - example

# print("The break instruction:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Inside the loop.", i)
# print("Outside the loop.")


# # continue - example

# print("\nThe continue instruction:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop.")
# break  example
print('break example')
# for i in range (1,10):
#     if i==5:
#         break
#     print ('inside the loop :',i)
#     print ('outside the loop')
#     print('\n continue with example')
#     for i in range (1,10):
#         if i==5:
#             continue
#         print ('inside the loop',i)
#         print('outside the loop')
largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")


