import db_driver

class Planet:
    '''
    Название планеты
    Радиус (км)
    Масса (кг)
    Расстояние от Солнца (млн км)
    Тип (каменная, газовый гигант, ледяной гигант)
    '''
    def __init__(self, 
                 name=None, 
                 radius=None, 
                 mass=None,
                 distance=None,
                 planet_type=None
                 ):
        
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = distance
        self.planet_type = planet_type

    def to_dict(self):
        return {"name":self.name, "radius": self.radius, "mass":self.mass,"distance": self.distance, "planet_type": self.planet_type }

def main():
    planet1 = Planet(
        name="e2", 
        radius=560, 
        mass=720,
        distance=15000,
        planet_type="каменная"
    )

    print(planet1.name)
    print(planet1.radius)
    print(planet1.mass)
    print(planet1.distance)
    print(planet1.planet_type)

def db_tester():
    pass


if __name__ == "__main__":
    db_tester()
    # main()