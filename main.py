from planet import Planet, PlanetCollection
from films import Film, FilmCollection

from menu import *

def main():
    print("Выберите коллекцию:")
    print("1 - Фильмы")
    print("2 - Планеты")
    print("3 - Выход")
    
    try:
        choice = int(input())
        
        if choice == 1:
            films_col = FilmCollection()
            films_menu(films_col)
        
        elif choice == 2:
            planets_col = PlanetCollection()
            planets_menu(planets_col)
        
        elif choice == 3:
            print("Выход из программы")
            return True
        
        else:
            print("Неверный выбор")
            return False
    
    except Exception as e:
        print(f"Ошибка: {e}")
        return False


if __name__ == "__main__":
    while True:
        if main():
            break