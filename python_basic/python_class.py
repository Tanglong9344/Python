# 类 class
'''
关键字class加上类名用来创建一个类。
之后缩进的代码块是这个类的内部。
在这里，我们用pass语句，表示一个空的代码块。
类名加圆括号()的形式可以创建一个类的实例，
也就是被称作对象的东西。我们把这个对象赋值给变量mc。
于是，mc现在就是一个MyClass类的对象。
'''
# 示例1
print("示例1:")
class MyClass:
    pass  # 表示类为空

mc = MyClass()
print(mc)

# 示例2
print("示例2:")
class MyClass:
    name = "Jake"

    def hello(self):
        print("Hello,I am %s" % self.name)

mc = MyClass()
print(mc)
print(mc.name)
mc.hello()

'''
调用类变量的方法是“对象.变量名”。
你可以得到它的值，也可以改变它的值。
注意到，类方法和我们之前定义的函数区别在于，
第一个参数必须为self。
而在调用类方法的时候，
通过“对象.方法名()”格式进行调用，
而不需要额外提供self这个参数的值。
self在类方法中的值，就是你调用的这个对象本身。
'''

# 示例3
# 问题描述：
'''
今天我用一个例子来展示两种程序设计方式的不同。
假设我们有一辆汽车，我们知道它的速度(60km/h)，
以及A、B两地的距离(100km)。要算出开着这辆车从A地到B地花费的时间。
'''
print("示例3.1,面向过程:")
speend = 60.0
distance = 100.0
time = distance / speend
print("Time: %f(hours)" % time)

print("示例3.2,面向对象:")
class Car:
    speend = 0.0

    def carTime(self, distance):
        time = distance / self.speed
        print("Time: %f(hours)" % time)

car = Car()
car.speed = 60.0
car.carTime(100.0)

# 示例4，继承
# 问题描述：
'''
仍然是从A地到B地，这次除了有汽车，我们还有了一辆自行车！
自行车和汽车有着相同的属性：速度（speed）。
还有一个相同的方法（drive），来输出行驶/骑行一段距离所花的时间。
但这次我们要给汽车增加一个属性：每公里油耗（fuel）。
而在汽车行驶一段距离的方法中，除了要输出所花的时间外，
还要输出所需的油量。

'''
print("示例4，继承：")
# 定义一个超类，包含自行车和汽车的基本属性
class Vehicle:
    # __init__函数会在类被创建的时候自动调用，
    # 用来初始化类。它的参数，要在创建类的时候提供。
    def __init__(self, speed):
        self.speed = speed

    def vehicle(self, distance):
        time = distance / self.speed
        print("Time: %f(hours)" % time)

# 定义自行车类
class Bike(Vehicle):
    pass

# 定义汽车类
class Car(Vehicle):
    def __init__(self, speed, fuel):
        Vehicle.__init__(self, speed)
        self.fuel = fuel

    def vehicle(self, distance):
        Vehicle.vehicle(self, distance)
        print("Fuel: %f(liters) " % (self.fuel * distance))

bike = Bike(15.0)
bike.vehicle(100.0)

car = Car(60.0, 0.012)
car.vehicle(100.0)