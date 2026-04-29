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
        self.planet_array = []

    def load(self):
        try:
            data = db.load_db()
            if data:
                self.planet_array = [] 
                self.add_list_planets(data)
                return True
            return False
        
        except Exception as e:
            print(f"Ошибка загрузки из БД: {e}")
            return False

    def get_array(self):
        return self.planet_array

    def apply(self):
        try:
            data_to_save = []
            for planet in self.planet_array:
                data_to_save.append(planet.to_dict() if isinstance(planet, Planet) else planet)
                    
            return db.save(data_to_save)
        
        except Exception as e:
            print(f"Ошибка сохранения в БД: {e}")
            return False

    def add_planet(self, planet: Planet):
        if not isinstance(planet, Planet):
            print(f"Ошибка, нельзя добавить объект типа{type(planet)}")
            return False
        if planet in self.planet_array:
            print(f"Ошибка, объект уже существует")
            return False
        self.planet_array.append(planet)
        return True
    
    def add_list_planets(self, arr_):

        for item in arr_:
            if isinstance(item, Planet):
                self.add_planet(item)

            elif isinstance(item, dict):
                try:
                    planet = Planet(
                        name=item.get('name', ''),
                        radius=item.get('radius', 0),
                        mass=item.get('mass', 0),
                        distance=item.get('distance', 0),
                        planet_type=item.get('planet_type', '')
                    )
                    self.add_planet(planet)
                except Exception as e:
                    print(f"Ошибка создания планеты из словаря: {e}")
            else:
                print(f"Неизвестный тип данных: {type(item)}")

    def delete_planet(self,planet):
        if planet in self.planet_array:
            self.planet_array.remove(planet)    
            return True
        
        print("Объект не найден в базе!")
        return False

    def get_count(self):
        return len(self.planet_array)
    

    def check_in_db(self, new_planet, exclude_name):
        for p in self.planet_array:
            if p.name == new_planet.name:
                if exclude_name and p.name == exclude_name:
                    continue 
                print(f"Планета с именем '{new_planet.name}' уже существует!")
                return True
            return False


    def edit_planet(self, old_name, new_planet):
        for i in range(self.get_count()):
            if self.planet_array[i].name == old_name:
                if old_name != new_planet.name:

                    if self.check_in_db(new_planet, exclude_name=old_name):
                        return False
                
                self.planet_array[i] = new_planet
                print(f"Планета '{old_name}' изменена на '{new_planet.name}'")
                return True
    
        print(f"Планета '{old_name}' не найдена")
        return False

    def get_planet(self, name):
        for planet in self.planet_array:
            if planet.name == name:
                return planet
        return None

    def show_all(self):
        for i in self.planet_array:
            print(i)


    def clear_all(self):
        self.planet_array.clear()


    ''' sort '''

    """
    def sort_planet(self, field_key="distance", reverse=False):
        def sorter(p):
            if field_key == "name":
                return p.name or ""  # Обработка None значений
            elif field_key == "radius":
                return p.radius or 0
            elif field_key == "mass":
                return p.mass or 0
            elif field_key == "planet_type":
                return p.planet_type or ""
            elif field_key == "distance":
                return p.distance or 0
            else:
                print(f"Неизвестное поле для сортировки: '{field_key}'. Сортирую по расстоянию")
                return p.distance or 0
        
        try:
            self.planet_array.sort(key=sorter, reverse=reverse)
            return True
        
        except Exception as e:
            print(f"Ошибка: {e}")
            return False
    """
    def sort_planet(self, field_key="distance", reverse=False):
        
        n = len(self.planet_array)
        for i in range(n):
            for j in range(0, n-i-1):
                planet1 = self.planet_array[j]
                planet2 = self.planet_array[j+1]
                
   
                if field_key == "name":
                    need_swap = planet1.name > planet2.name
                elif field_key == "radius":
                    need_swap = planet1.radius > planet2.radius
                elif field_key == "mass":
                    need_swap = planet1.mass > planet2.mass
                elif field_key == "distance":
                    need_swap = planet1.distance > planet2.distance
                elif field_key == "planet_type":
                    need_swap = planet1.planet_type > planet2.planet_type
                else:
                    print(f"Неизвестное поле для сортировки: '{field_key}'. Сортирую по расстоянию")
                    need_swap = planet1.distance > planet2.distance
                
                if reverse:
                    need_swap = not need_swap
                
                if need_swap:
                    self.planet_array[j], self.planet_array[j+1] = self.planet_array[j+1], self.planet_array[j]
        
        return True

