"""a = [1,2,3,4]
for i in a:
    if i==1:
        del a[2]
print(i)"""

"""i = "this won't stay"
for i in range(5):
    pass
print(i)"""

"""a, *b = "hjkhjkh"
print(a)"""

"""a = [1,2,3]
b = [1,2,3,4,5,6]
print(list(zip(a, b)))
for x, y in zip(a, b):
    print(x, y)"""


class Car:
    def __init__(self, number):
        self.number = number


lst = list()
for x in range(10):
    lst.append(Car(x))
b = 4
