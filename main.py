from planet import Planet, PlanetCollection
from films import Film, FilmCollection

from menu import *

def main():
    films_col = FilmCollection()
    run_program = True

    print_menu()

    while run_program:
        print("С какими объектами будем работать?")
        print("1 фильмы")
        print("2 планеты ")
        try:
            ans = int(input())
            if ans == 1:
                if films_menu(films_col):
                    run_program = False
            elif ans == 2:
                pass
            else:
                raise ValueError("Нет такого варианта!")
        except Exception as e:
            print("Ошибка, неправильный ввод")


if __name__ == "__main__":
    main()
