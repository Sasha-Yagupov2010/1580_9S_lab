import db_driver as db

# planet.py
import json

class Planet:
    _id_counter = 0
    
    def __init__(self, name=None, radius=None,  mass=None, distance=None, planet_type=None):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = distance
        self.planet_type = planet_type

        self.__id = Planet._id_counter
        Planet._id_counter += 1
        print(f"Создание ID {self.__id}")


    def __str__(self):
        return (f"Планета '{self.name}' (ID: {self.__id}): "
                f"Радиус={self.radius} км, Масса={self.mass} кг, "
                f"Расстояние={self.distance} млн км, Тип='{self.planet_type}'")

    def __repr__(self):
        return f"Planet(name='{self.name}', radius={self.radius}, mass={self.mass}, distance={self.distance}, type='{self.planet_type}')"

    def __copy__(self):
        return Planet(
            name=self.name,
            radius=self.radius,
            mass=self.mass,
            distance=self.distance,
            planet_type=self.planet_type
        )

    def __del__(self):
        print(f"Удаление ID {self.__id}")

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.distance > other.distance

    def __le__(self, other):
        return self.distance <= other.distance

    def __ge__(self, other):
        return self.distance >= other.distance

    def to_dict(self):
        return {
            "name": self.name,
            "radius": self.radius,
            "mass": self.mass,
            "distance": self.distance,
            "planet_type": self.planet_type 
        }
    
    @staticmethod
    def get_planet_types():
        return ["каменная", "газовый гигант", "ледяной гигант"]

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            radius=data.get("radius"),
            mass=data.get("mass"),
            distance=data.get("distance"),
            planet_type=data.get("planet_type")
        )

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
    planet1 = Planet(
        name="1", 
        radius=5621230, 
        mass=72123213210,
        distance=150013321230,
        planet_type="каменная"
    )
    planet2 = planet1.__copy__()
    print(planet2)
    



if __name__ == "__main__":
    #main()
    db_tester()