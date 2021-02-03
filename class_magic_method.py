print(3.3 + 4.4)
print(3.3.__add__(4.4))

print(len([1, 2, 3]))
print([1, 2, 3].__len__())

print("h" in "hello")
print("hello".__contains__("h"))

# String representation with __str__ and __repr__ method
class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f'Card("{self.rank}", "{self.suit}")'

c = Card("Ace", "Spades")
print(c) # it'll execute the __str__ or __repr__ method

print(c.__str__())
print(c.__repr__())


# Equality with __eq__ method
class Student():
    def __init__(self, maths, history, writing):
        self.maths = maths
        self.history = history
        self.writing = writing

    @property
    def grades(self):
        return self.maths + self.history + self.writing

    def __eq__(self, other_student):
        return self.grades == other_student.grades

bob = Student(maths = 90, history = 90, writing = 90)
moe = Student(maths = 100, history = 90, writing = 80)
joe = Student(maths = 40, history = 45, writing = 70)

print(bob.grades)
print(moe.grades)

print(bob == moe)
print(moe == bob)
print(bob == joe)
print(moe == joe)

print(bob != joe)
print(joe != moe)


# the namedtuple object
import collections

Book = collections.namedtuple("Book", ["title", "author"])

animal_farm = Book("Animal Farm", "George Orwell")
gatsby = Book(title = "The Great Gatsby", author = "F. Scott Fitzgerald")

print(animal_farm[0])
print(gatsby[1])
print(animal_farm.title)
print(gatsby.author)


# Name mangling for privacy
class Nonsense():
    def __init__(self):
        self.__some_attribute = "Hello"

    def __some_method(self):
        print("This is coming from some_method!")

class SpecialNonsense(Nonsense):
    pass

n = Nonsense()
sn = SpecialNonsense()

print(n._Nonsense__some_attribute)
print(sn._Nonsense__some_attribute)
(n._Nonsense__some_method())
(sn._Nonsense__some_method())


# Multiple inheritance I
class FrozenFood():
    def thaw(self, minutes):
        print(f"Throwing for {minutes} minutes")

    def store(self):
        print("Putting in the freezer!")

class Dessert():
    def add_weight(self):
        print("Putting on the pounds!")

    def store(self):
        print("Putting in the refrigerator!")

class IceCream(Dessert, FrozenFood):
    pass

ic = IceCream()
ic.add_weight()
ic.thaw(5)
ic.store()

print(IceCream.mro()) # to get the order of the class whose methods are gonna get the preffernces


# Multiple inheritance: Breadth first search and Depth for search

class Restraunrant():
    def make_reservation(self, party_size):
        print(f"Booked a table for {party_size}")

class Steakhouse(Restraunrant):
    pass

class Bar():
    def make_reservation(self, party_size):
        print(f"Booked a lounge for {party_size}")

class BarAndGrill(Steakhouse, Bar):
    pass

bag = BarAndGrill()
bag.make_reservation(2)
print(BarAndGrill.mro())


#Multiple inheritance: Diamond shaped
class FilmMaker():
    def give_interview(self):
        print("I love making movies!")

class Director(FilmMaker):
    pass

class Screenwriter(FilmMaker):
    def give_interview(self):
        print("I love writing scripts!")

class JackOfAllTrades(Screenwriter, Director):
    pass

stallone = JackOfAllTrades()
stallone.give_interview()

print(JackOfAllTrades.mro())


# isintance is a function to check if the first argument is an instance made from the subclass or superclass of the second argument

print(isinstance([], list))
print(isinstance({}, dict))
print(isinstance([], (list, dict, int)))

class Person():
    pass

class Superhero(Person):
    pass

arnold = Person()
boris = Superhero()

print(isinstance(boris, Superhero))
print(isinstance(boris, Person))
print(isinstance(arnold, Person))
print(isinstance(arnold, Superhero))

print(issubclass(Superhero, Person))
print(issubclass(Person, Superhero))
print(issubclass(Superhero, object))
print(issubclass(Person, Superhero))


# Composition
class Paper():
    def __init__(self, text, case):
        self.text = text
        self.case = case

class Briefcase():
    def __init__(self, price):
        self.price = price
        self.papers = []

    def add_paper(self, paper):
        self.papers.append(paper)

    def view_notes(self):
        return [paper.text for paper in self.papers]

class Lawyer():
    def __init__(self, name, briefcase):
        self.name = name
        self.briefcase = briefcase

    def write_notes(self, text, case):
        paper = Paper(text, case)
        self.briefcase.add_paper(paper)

    def view_notes(self):
        print(self.briefcase.view_notes())

cheap_briefcase = Briefcase(price = 19.99)
vinny = Lawyer(name = "Vincent", briefcase = cheap_briefcase)

vinny.write_notes("My client is innocent!", "AS-2ZK1")
vinny.write_notes("There is no evidence of a cirme!", "AS-2ZK1")
vinny.view_notes()

print("this file is now complete")
print("in dev branch")

print("New change in dev branch")