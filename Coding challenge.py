# Coding challenge 
#Q1
class Planet:
    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type
    
    def get_distance_to_earth(self):
        #Sun to Earth in Km
        distance_to_earth_from_sun = 147_000_000
        # distance to Earth
        return {'distance to earth': abs(self.distance_from_sun - distance_to_earth_from_sun)}


#Q2
class Planet:
    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type
    
    def get_distance_to_earth(self):
        distance_to_earth_from_sun = 147_000_000
        return {'distance to earth': abs(self.distance_from_sun - distance_to_earth_from_sun)}

class Mercury(Planet):
    def __init__(self):
        super().__init__("Mercury", 58_000_000, "Terrestrial")
    
    @staticmethod
    def happy_new_year():
        return "A year on Mercury lasts 88 Earth days."

# Mercury object
mercury = Mercury()

# Print info 
print(f"Name: {mercury.name}")
print(f"Distance from Sun: {mercury.distance_from_sun} km")
print(f"Planet Type: {mercury.planet_type}")

print(mercury.get_distance_to_earth())
print(Mercury.happy_new_year())

#Q3
class Planet:
    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type
    
    def get_distance_to_earth(self):
        return {'distance to earth': abs(self.distance_from_sun - 147_000_000)}

class Jupiter(Planet):
    def __init__(self):
        super().__init__("Jupiter", 779_000_000, "Gas Giant")
        self.number_of_moons = 80
    
    @staticmethod
    def happy_new_year():
        return "A year on Jupiter lasts 4383 Earth days."

# Create Jupiter object
jupiter = Jupiter()

# Print info
print(f"Name: {jupiter.name}")
print(f"Distance from Sun: {jupiter.distance_from_sun} km")
print(f"Planet Type: {jupiter.planet_type}")
print(f"Number of Moons: {jupiter.number_of_moons}")
print(jupiter.get_distance_to_earth())
print(Jupiter.happy_new_year())