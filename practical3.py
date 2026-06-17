# class student:
#     #method to create a constructor
#     def __init__(self,name):
#         self.name =name
#         print("this is a constructor")
# st=student("anurag")
# print("object created",st.name,"and",st.age)
# class student:
#     #method to create a constructor
#     def __init__(self,name):
#         self.name =name
#         self.age =0
#         print("this is a constructor")

# st=student("anurag")
# st.age=10
# print("object created",st.name,"and",st.age)

# #inheritance in python
# class Parent:
#     def display(self):
#         print("this is a parent class")
# class Child(Parent):
#     pass

# obj=Child()
# # obj.display()

# class father:
#     def display(self):
#         print("this is father class")

# class mother:
#     def display2(self):
#         print("this is mother class")

# class child(father,mother):
#     pass

# obj=child()
# obj.display()
# obj.display2()

# class grandfather:
#     def display(self):
#         print("this is grandparent")
# class parent(grandfather):
#     def display2(self):
#         print("this is a parent class")
# class child(parent):
#     pass
# obj=child()
# obj.display()
# obj.display2()
# this is hierachical
# class parent:
#     def display(self):
#         print("this is parent class")
# class child1(parent):
#     def display2(self):
#         print("this is a child1 class")
# class child2(parent):
#     def display3(self):
#         print("this is child2 class")

# obj1=child1()
# obj2=child2()
# obj1.display()
# obj2.display()
# obj1.display2()
# obj2.display3()

# hybrid model
# class a:
#     def display(self):
#         print("A")
# class b(a):
#     pass
# class c(a):
#     pass
# class d(b,c):
#     pass

# obj=d()
# obj.display()


# class animal:
#     def sound(self):
#         print("animal sound")
# class dog(animal):
#     def sound(self):
#         print("bark ")
# class lion(animal):
#     def sound(self):
#         print("roar")

# l1=lion()
# l1.sound()
# d1=dog()
# d1.sound()
# a1=animal()
# a1.sound()
#polymorphism
# class dog:
#     def sounds(self):
#         print("bark")

# class lion:
#     def sounds(self):
#         print("roar")

#  d=dog()
#  l=lion()
#  d.sounds()
#  l.sounds()
# animals=[dog(),lion()]
# for animal in animals:
#     animal.sounds()
#encapsulation
# class student:
#     def __init__(self):
#         self.__marks=101
#     def getMarks(self):
#         return self.__marks
# s=student()
# print(s.getMarks())
# from abc import ABC , abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class car(Vehicle):
#     def start(self):
#         print("car started")
# c= car()
# c.start()
