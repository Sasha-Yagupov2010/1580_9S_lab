from planet import Planet, PlanetCollection

def main():
    pass


def planet_collection_demo():
    collection = PlanetCollection()
    
    print("Загрузка из БД")
    if collection.load():
        print(f"Загружено планет: {collection.get_count()}")
    else:
        print("Ошибка загрузки из БД")
    

    print("Добавление планет")
    planets_to_add = [
        Planet("Марс", 3389, 6.39e23, 227.9, "каменная"),
        Planet("Земля", 6371, 5.97e24, 149.6, "каменная"),
        Planet("Юпитер", 69911, 1.898e27, 778.5, "газовый гигант")
    ]
    
    collection.add_list_planets(planets_to_add)
    

    print("Сравнение планет")
    earth = collection.get_planet("Земля")
    mars = collection.get_planet("Марс")
    
    if earth and mars:
        print(f"Сравнение Земли и Марса:")
        print(f"Радиус: Земля ({earth.radius}) > Марс ({mars.radius}) = {earth.radius > mars.radius}")
        print(f"Масса: Земля ({earth.mass}) > Марс ({mars.mass}) = {earth.mass > mars.mass}")
        print(f"Расстояние: Земля ({earth.distance}) > Марс ({mars.distance}) = {earth.distance > mars.distance}")
    
    print("Сортировка по имени")
    collection.sort_planet(field_key="name",reverse=False)
    collection.show_all()
    
    print("Сортировка по массе")
    collection.sort_planet("mass", reverse=True)
    collection.show_all()
    

    print("Сортировка по расстоянию")
    collection.sort_planet("distance")
    collection.show_all()
    
    print("Сохранение в БД")
    if collection.apply():
        print(f"Всего планет: {collection.get_count()}")
    else:
        print("Ошибка сохранения в БД")
    

if __name__ == "__main__":
    planet_collection_demo()