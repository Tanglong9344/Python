# class variables and object variables


class Person:
    '''Represents a person.'''
    population = 0  # class variable

    def __init__(self, name):  # be called when a object is created
        '''Initializes the person's data.'''
        self.name = name  # object variable
        print('(Initializing %s)' % self.name)
        # When this person is created, he/she
        # adds to the population
        Person.population += 1

    def __del__(self):  # be called when a object is destroyed and there is no guarantee when that method will be run.
        '''I am leaving.'''
        print('%s says bye.' % self.name)
        Person.population -= 1
        if Person.population == 0:
            print('I am the last one.')
        else:
            print('There are still %d people left.' % Person.population)

    def sayhi(self):
        '''Greeting by the person.
        Really, that's all it does.'''
        print('Hi, my name is %s.' % self.name)

    def howmany(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print('I am the only person here.')
        else:
            print('We have %d persons here.' % Person.population)


p1 = Person('Tanglong001')
p1.sayhi()
p1.howmany()
p2 = Person('Tanglong002')
p2.sayhi()
p2.howmany()
