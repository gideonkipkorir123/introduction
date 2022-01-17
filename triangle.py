# def is_a_triangle(a, b, c):
#     if a + b <= c or  b + c <= a or  c + a <= b:
#         return False
       
#     return True

# x=is_a_triangle
# print(x(1, 1, 1))
# print(x(1, 1, 3))
def is_a_triangle(a,b,c):
    return a+b>c and b+c>a and c+a>b 
a=float(input('enter value of a :'))
b=float(input('enter value of b :'))    
c=float(input('enter value of c :'))
if is_a_triangle(a,b,c):
    print('it is a triangle')
else:
    print('it is not a triangle')    