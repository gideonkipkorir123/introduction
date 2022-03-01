a={1,2,3,5,7,9,10,111}
b={2,4,6,8}
c={1,2,3,5,7}
# x=odd.union(evens)
# print(x)
# y=odd.intersection(prime)
# print(y)
# z=odd.difference(prime)
# print(z)
# a=odd.symmetric_difference(prime)
# print(a)
# b=prime.update(evens)
# print(b)
x=c.update(a)
print(x)
y=c.intersection_update(a)
# intersection checks whether there are similar values in the sets
print(y)
print(c.issubset (a)) 
print(a.issuperset (b))
print(c.isdisjoint (a))
# disjoint returns a value if two sets have null intersections
# subset checks whether the above sets are similar

z=frozenset([1,2,3,4,5,6,7,8,9])
print(z)