import db_driver as db

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

        # self.__id

    @staticmethod
    def get_planet_types():
        return ["каменная", "газовый гигант", "ледяной гигант"]    


    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __copy__(self):
        pass

    def __del__(self):
        pass

    def __lt__(self):
        pass

    def __eq__(self):
        pass

    def __gt__(self):
        pass

    def __le__(self):
        pass

    def __ge__(self):
        pass

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
    planet1 = Planet(name="del")
    planet2 = Planet(name="2", mass=54)
    print(db.load_db())
    print(db.show_db())
    
    db.add_obj(planet1)
    print(db.get_object(planet1.name))
    db.edit_obj(planet2,planet1)
    print(db.get_object(planet2.name))
    print(db.get_object(planet1.name))
    db.del_obj(planet2)
    print(db.show_db())



if __name__ == "__main__":
    main()
    db_tester()