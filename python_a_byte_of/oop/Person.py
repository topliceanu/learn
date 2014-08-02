class Person:
    """ Represents an person's stored data. """

    population = 0

    def __init__ (self, name):
        self.name = name
        Person.population += 1

    def hi(self):
        print 'Hi, my name is {0}'.format(self.name)

    def credentials(self):
        return (self.name, 'pfa')
