# def happy_new_year(wishes = False):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return
    
#     print("Happy New Year!")
# happy_new_year()    
# # When used inside a function, it causes the immediate termination of the function's execution, and an instant return (hence the name) to the point of invocation.

# Note: if a function is not intended to produce a result, using the return instruction is not obligatory - it will be executed implicitly at the end of the function.

# Anywaye_you_soon can use it to terminate a function's activities on demand, before the control reaches the function's last line.
# def new_year(wishes):
#     print('please come back home.....')
#     return 2021
# print('happy new year')
# def new_year(wishes): 
#     print()  

# def boring_function():
#      print("'Boredom Mode' ON.")
#      return 123
# print("This lesson is interesting!")
# boring_function()
# print("This lesson is boring...")
       
def list_sum(lst):
    s = ''
    
    for elem in lst:
        s += elem
    
    return s  
list1 = 'word' 
func = list_sum(list1)       
print('sum of elements',func)  