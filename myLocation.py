class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")

# First instantiation of the Location class
loc = Location("Catherine", "Indonesia")
loc1 = Location("Tomas", "Portugal")
loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")
print(loc.name)
print(loc.country)
print(type(loc))
# Call a method from the instantiated class
loc.myLocation()
loc1.myLocation()
# Three more instantiations and method calls for the Location class
loc2.myLocation()
loc3.myLocation()
your_loc = Location("Catherine.E.J", "Indonesia")
your_loc.myLocation()
