# student_name=input("Enter your fulll name : ")
# print("your name is : ",student_name)
# #admission=int(input("enter your admission : "))
# adm=input("enter your reg number")
# print("Your full details are"+student_name,adm)
def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

print(create_list(5))

