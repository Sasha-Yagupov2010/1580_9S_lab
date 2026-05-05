from planet import Planet, PlanetCollection
from films import Film, FilmCollection
import csv

def check_mode(mode):
    if not (1<=mode<=10):
        print("Ошибка! нет выбранного режима")
        return False
    
    return True


def check_year(year):
    return year>1888

def check_score(score):
    return 0<=score<=10

def check_length(length):
    return length>0

def interactive_creating():
    try:
        print("Введи название фильма")
        name=input()

        print("Введи режжисера фильма")
        rezhiser=input()

        print("Введи год фильма")
        year=int(input())

        print("Введи рейтинг фильма")
        score=int(input())

        print("Введи продолжительность фильма")
        length=int(input())

        print("Введи категорию фильма")
        film_type=input()

        if not check_year(year):
            raise ValueError("Неверный год")
        
        if not check_score(score):
            raise ValueError("Неверный рейтинг")
        
        if not check_length(length):
            raise ValueError("Неверная длина")
       
        print("фильм успешно создан")
        return Film(name,rezhiser,year,score,length,film_type)
    
    except Exception as e:
        print(f"Ошибка ввода: {e}")
        return None
    
    return Film()
 

def write_CSV(filename, mycollection):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Название", "Режиссер", "Год", "Рейтинг", "Продолжительность", "Категория"])
            
            for film in mycollection.get_array():
                writer.writerow([
                    film.name,
                    film.rezhiser,
                    film.year,
                    film.score,
                    film.length,
                    film.film_type
                ])
        
        print(f"Данные успешно экспортированы в {filename}")
        return True
    
    except Exception as e:
        print(f"Ошибка: {e}")
        return False         



def main():
    collection = FilmCollection()
    run_program = True

    while run_program:
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
                if collection.get_count() == 0:
                    print("Коллекция фильмов пуста.")
                else:
                    collection.show_all()

            elif mode == 4: 
                new_film = interactive_creating()
                if new_film is not None:
                    collection.add_film(new_film)
                else:
                    print("Ошибка создания")    

            elif mode == 5: 
                if collection.get_count() == 0:
                    print("Коллекция фильмов пуста.")
                else:
                    data = input()
                    l = collection.search(data)
                    if l:
                        for i in l:
                            print(i)
                    print("Не найдено")        

            elif mode == 6: 
                if collection.get_count() == 0:
                    print("Коллекция фильмов пуста.")
                else:
                    new_film = interactive_creating()

                    if new_film is not None:
                        old_film = input()
                        collection.edit_film(old_film,new_film)
                    else:
                        print("Ошибка замены")    


            elif mode == 7:
                if collection.get_count() == 0:
                    print("Коллекция фильмов пуста.")
                else:
                    name = input()
                    film_to_delete = collection.get_film(name)
                    if film_to_delete:
                        if collection.delete_film(film_to_delete):
                            print(f"Фильм '{name}' удален")
                        else:
                            print(f"Не удалось удалить фильм")
                    else:
                        print(f"Фильм не найден!")
  

            elif mode == 8:
                if collection.get_count() == 0:
                    print("Коллекция фильмов пуста.")
                else:
                    field = input()
                    collection.sort_film(field)

                    collection.show_all()

            elif mode == 9:
                if collection.get_count() == 0:
                    print("Коллекция фильмов пуста.")
                else:
                    filemame = input()
                    write_CSV(filemame,collection)

            else:
                run_program = False
                

        except Exception as e:
            print(f"Ошибка {e}")
            continue 

    
if __name__ == "__main__":
    main()
