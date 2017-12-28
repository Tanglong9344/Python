# python object
# basic class
class Person:
    'A person class'
    # initialize class method
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    # show information of a person
    def show(self):
        print("Name:",self.name, ", Age:", self.age)

# create and visit
p = Person("Tanglong", 18)
print(p.name)
print(p.age)
p.show()
# modify
p.age = 19
p.name = "longTang"
p.show()

# attributes in class
print(hasattr(p,"addr"))
setattr(p,"addr","hangzhou")
print(hasattr(p,"addr"))
delattr(p,"addr")
print(hasattr(p,"addr"))

# build-in attributes
print("doc   : ",Person.__doc__)
print("name  : ",Person.__name__)
print("module: ",Person.__module__)
print("bases : ",Person.__bases__)
print("dict  : ",Person.__dict__)

# __del__ && del
class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = Point()
print (id(pt1), id(pt2), id(pt3));   # print the id of the obejcts, and pt1 equals pt2
del pt1
del pt2
del pt3

# extends class
class Parent:
    def show(self):
        print("Parent...")

class Child(Parent):
    def show(self):
        Parent().show()
        print("Child...")

c = Child()
c.show()

print("isinstance: ",isinstance(c,Child))
print("issubclass: ",issubclass(Child, Parent))

# overload operator
class Operator:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Operator(%d, %d)' % (self.a, self.b)

   def __add__(self,other):
      return Operator(self.a + other.a, self.b + other.b)

o1 = Operator(3,4)
print(o1.__str__())
o2 = Operator(-3,5)
print(o2)
print (o1 + o2)

# hide data in class
class HideAge:
    'A person class that hide name'
    # initialize class method
    def __init__(self, name, age):
        self.name = name
        self.__age  = age # hide age
    # show information of a person
    def show(self):
        print("Name:",self.name, ", Age:", self.__age)

ha = HideAge("Tanglong", 110)
print(ha.name)
ha.show()

