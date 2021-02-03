# declaration of a class
class Person():
    pass 

class DatabaseConnection():
    pass

boris = Person()
sally = Person()

print(boris)
print(sally)

database_connection = DatabaseConnection()
print(database_connection)

# The __init__ method
class Guitar():
    def __init__(self):
        print(f"A new guitar is being created! This object is {self}")

acoustic = Guitar()
print(acoustic)

electric = Guitar()
print(electric)

acoustic.wood = "Mahogany"
acoustic.strings = 6
acoustic.year = 1990

electric.nickname = "Sound viking 3000"

print(acoustic.wood)
print(electric.nickname)

# print(electric.year)


# Instance method 
class Pokemon():
    def __init__(self, name, specialty, health = 100):
        self.name = name
        self.specialty = specialty
        self.health = health

    def roar(self):
        print("Raaaarr!")

    def describe(self):
        print(f"I am {self.name}. I am a {self.specialty} Pokemon.")
    
    def take_damage(self, amount):
        self.health -= amount

squirtle = Pokemon("Squirtle", "Water")
charmander = Pokemon(name = "Charmander", specialty = "Fire", health= 110)
squirtle.roar()
charmander.roar()
squirtle.describe()
charmander.describe()

print(squirtle.health)
squirtle.take_damage(20)
print(squirtle.health)


# Protected Attributs and methods
class SmartPhone():
    def __init__(self):
        self._company = "Apple"
        self._firmware = 10.0

    def get_os_version(self):
        return self._firmware

    def update_firmware(self):
        print("Reaching out to the server for the next version")
        self._firmware += 1

iphone = SmartPhone()
print(iphone._company)
print(iphone._firmware)

print(iphone.update_firmware())
print(iphone._firmware)


# properties with property method
class Height():
    def __init__(self, feet):
        self._inches = feet * 12

    def _get_feet(self):
        return self._inches / 12

    def _set_feet(self, feet):
        if feet >= 0:
            self._inches = feet * 12

    feet = property(_get_feet, _set_feet)

h = Height(5)
print(h.feet)

h.feet = 6
print(h.feet)

h.feet = -10
print(h.feet)


# Alternate approach
class Currency():
    def __init__(self, dollars):
        self._cents = dollars * 100

    @property
    def dollars(self):
        return self._cents / 100

    @dollars.setter
    def dollars(self, dollars):
        if dollars >= 0:
            self._cents = dollars * 100

bank_account = Currency(50000)
print(bank_account.dollars)

bank_account.dollars = 100000
print(bank_account.dollars)

bank_account.dollars = -20000
print(bank_account.dollars)


# the getattr and setattr function
stats = {
    "name": "BBQ Chicken",
    "price": 19.99,
    "size": "Extra Large",
    "ingredients": ["Chicken", "Onions", "BBQ Sauce"]
}

class Pizza():
    def __init__(self, stats):
        for key, value in stats.items():
            setattr(self, key, value)

bbq = Pizza(stats)

print(bbq.size)
print(bbq.ingredients)

for attr in ["price", "name", "diameter", "discounted"]:
    print(getattr(bbq, attr, "Unknown"))


# The hasattr and delattr method
stats_to_delete = ["size", "diameter", "spiciness", "ingredients"]

print(bbq.size)

for stat in stats_to_delete:
    if hasattr(bbq, stat):
        delattr(bbq, stat)

# print(bbq.size) # It'll raise an error as attribute size has been deleted

