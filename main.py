from planet import Planet, PlanetCollection
from films import Film, FilmCollection
import csv

def check_mode(mode):
    if not (mode > 0 and mode < 11):
        print("Ошибка! нет выбранного режима")
        return False
    
    return True

def interactive_creating():
    return Film()


def write_CSV(filename, mycollection):
    try:
        with open('filename', 'w') as csv_file:
            for row in mycollection.get_array():
                print(row,file=csv_file)
    except Exception as e:
        print(e)
        return False
    
    return True            

run_program = True

def main():
    collection = FilmCollection()

    print("check_mode:")
    print("""
1 - Загрузка БД из файла
2 - Сохранение БД в файл
3 - Просмотр всех записей
4 - Добавление новой записи
5 - Поиск записи (по разным критериям)
6 - Редактирование записи
7 - Удаление записи
8 - Сортировка (по разным полям)
9 - Экспорт в CSV
10- Выход
          """)
    
    try:
        mode = int(input())
        if not check_mode(mode):
            raise ValueError
        
        if mode == 1:
            collection.load()

        elif mode == 2: 
            collection.apply()

        elif mode == 3: 
            collection.show_all()

        elif mode == 4: 
            new_film = interactive_creating()
            collection.add_film(new_film)

        elif mode == 5: 
            data = input()
            print(collection.search(data))

        elif mode == 6: 
            new_film = interactive_creating()
            old_film = input()
            collection.edit_film(old_film,new_film)

        elif mode == 7:
            name = input()
            collection.delete_film(name)    

        elif mode == 8:
            field = input()
            collection.sort_film(field)

        elif mode == 9:
            filemame = input()
            write_CSV(filemame,collection)

        else:
            run_program = False
            

    except Exception as e:
        print("Ошибка ввода")
        return    

     


if __name__ == "__main__":
    while run_program:
        main()
