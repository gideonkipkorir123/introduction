# def message():
#     print('we start here')
# message()
# print('we end here')
# how functions communicate with their environment
#   
# def introduction(first_name,second_name):
#     print('my name is :',first_name,second_name)
# introduction('Gideon','Kipkorir')
# introduction('Mark','kiplimo')
    
# def address(street, city, postal_code):
#     print("Your address is:", street, "St.,", city, postal_code)

# s = input("Street: ")
# p_c = input("Postal Code: ")
# c = input("City: ")

# address(s, c, p_c)
# def home(street,city,home_address):
#     print('Your exact home location is :',city,street,home_address)
# a=input('home city :')
# b=input("home street :")
# c=input('home address :')  

# home(b,a,c)

def home(city,street,address):
    print("enter your exact location adreess: ",city,street,address)
a=input('enter your neares town:')
b=input("enter your nearest street :")
c=input('enter your home address')
home(a,b,c)    