class Planet:
    def __init__(self, name, planet_type, star):
        self.name = name
        self.planet_type = planet_type
        self.star= star

        self.check_planet()
    def orbit(self):
        return f"{self.name} is orbitting around {self.star}..."
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"
    
    def check_planet(self):
        if not all(isinstance(x, str) for x in (self.name, self.planet_type, self.star)):
            raise TypeError("name, planet type, and star must be strings")
        if "" in (self.name, self.planet_type, self.star):
            raise ValueError("name, planet_type, and star must be non-empty strings")

planet_1 = Planet("Earth", "Terrestrial", "Sun")
planet_2 = Planet("Jupiter", "Gas Giant", "Sun")
planet_3 = Planet("Proxima b", "Exoplanet", "Proxima Centauri")
#planet_4 = Planet(3, "Exoplanet", "Kepler-22")

print(planet_1, planet_2, planet_3, sep="\n")
print(planet_1.orbit(), planet_2.orbit(), planet_3.orbit(), sep="\n")