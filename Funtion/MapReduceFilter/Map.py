import math

def area(r):
    """Area of a circle with radius r ."""
    return math.pi * (r**2)

radii = [2, 4, 5, 6, 7]

#Direct method

# areas = []
# for r in radii:
#     a = area(r)
#     areas.append(a)
#
# print(areas)

#With map function

map_obj = map(area, radii)
lst = list(map_obj)
print(lst)

# why use map
#eg if you want to convert cel to farh

temp = [("Mumbai", 23), ("Pune", 21), ("Rajasthan", 32), ("Indore", 26)]

c_to_f = lambda data: (data[0], (9/5) * data[1] + 32)

lst1 = list(map(c_to_f, temp))
print(lst1)








