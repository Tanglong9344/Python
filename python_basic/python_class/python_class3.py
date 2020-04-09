class Person:
    '''Represents a person.'''
    population = 0

    def __init__(self, name):  # be called when a object is created
        self.name = name
        print('(Initialization %s)' % self.name)
        Person.population += 1

    def __del__(self):  # be called when a object is destroyed and there is no guarantee when that method will be run.
        print('%s says goodbye.' % self.name)
        Person.population -= 1
        if Person.population == 0:
            print('I am the last one.')
        else:
            print('There are still %d people left.' % Person.population)

    def sayhi(self):
        print('Hi, my name is %s.' % self.name)

    def howmany(self):
        if Person.population == 1:
            print('There is only one person left.')
        else:
            print('We have %d persons here.' % Person.population)


p1 = Person('Tang long 001')
p1.sayhi()
p1.howmany()

p2 = Person('Tang long 002')
p2.sayhi()
p2.howmany()