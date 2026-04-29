import db_driver as db

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


class PlanetCollection:
    def __init__(self):
        planet_array = []

    def load(self):
        self.planet_array = db.load_db()
        return True

    def get_array(self):
        return self.planet_array

    def upply(self):
        return db.save(self.planet_array)

    def add_planet(self, planet: Planet):
        if isinstance(planet, Planet):
            self.planet_array.append(planet)
            return True
        print(f"Ошибка, нельзя добавить объект типа{type(planet)}")
        return False


    def delete_planet(self,planet):
        if planet in self.planet_array:
            self.planet_array.remove(Planet)    
            return True
        
        print("Объект не найден в базе!")
        return False

    def edit_planet(self):
        pass

    def get_planet(self):
        pass

    def show_all(self):
        for i in self.planet_array:
            print(i)

    def get_cout(self):
        return len(self.planet_array)

    def clear_all(self):
        self.planet_array = []
        

    ''' sort '''

    def sort_planet(self, field_key="distance"):
        pass

