from planet import Planet, PlanetCollection
from films import Film, FilmCollection
import csv

def check_mode(mode):
    if not isinstance(mode,int):
        print("Ошибка! неверный тип данных")
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

        print("Введи режиссера фильма")
        rezhiser=input()

        print("Введи год фильма")
        year=int(input())

        print("Введи рейтинг фильма")
        score=int(input())

        print("Введи продолжительность фильма")
        length=int(input())

        print("Введи категорию фильма")
        film_type=input()

        if not name:
            raise ValueError("Название не может быть пустым")
        if not rezhiser:
            raise ValueError("Режиссер не может быть пустым")
        if not film_type:
            raise ValueError("Категория не может быть пустой")
        
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



def print_menu():
        print("Выберите действие:")
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


def main():
    collection = FilmCollection()
    run_program = True

    print_menu()
    
    while run_program:    
        try:
            mode = int(input())
            if not check_mode(mode):
                raise ValueError("Некорректный ввод")
            
            if mode == 1:
                collection.load()

            elif mode == 2: 
                collection.apply()
                print("Сохранено.")

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
                    print("Введите информацию для поиска")
                    data = input()
                    l = collection.search(data)
                    if l:
                        for i in l:
                            print(i)
                    else:        
                        print("Не найдено")        

            elif mode == 6: 
                if collection.get_count() == 0:
                    print("Коллекция фильмов пуста.")
                else:
                    print("Введите название фильма для редактирования:")
                    old_film_name = input()
                    
                    # Проверить, существует ли фильм
                    old_film = collection.get_film(old_film_name)
                    if not old_film:
                        print(f"Фильм '{old_film_name}' не найден!")
                        continue
                    
                    print(f"Редактирование фильма '{old_film_name}'")
                    new_film = interactive_creating()
                    if new_film is not None:
                        collection.edit_film(old_film_name, new_film)
                    else:
                        print("Ошибка замены") 


            elif mode == 7:
                if collection.get_count() == 0:
                    print("Коллекция фильмов пуста.")
                else:
                    print("Введите название для удаления")
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
                    print("Выберите поле для сортировки:")
                    print("name - по названию")
                    print("rezhiser - по режиссеру")
                    print("year - по году")
                    print("score - по рейтингу")
                    print("length - по продолжительности")
                    print("film_type - по категории")

                    try:    
                        field = input("Введите поле для сортировки: ")
                        
                        print("Обратная сортировка? (y/n): ")
                        reverse_input = input().strip().lower()
                        reverse = reverse_input in ["y", "yes", "true", "1", "да"]
                        
                        if collection.sort_film(field, reverse):
                            print(f"Сортировка по '{field}' выполнена:")
                            collection.show_all()
                        else:
                            print(f"Не удалось отсортировать по полю '{field}'")
                    except Exception as e:
                        print(f"Ошибка сортировки: {e}")


            elif mode == 9:
                if collection.get_count() == 0:
                    print("Коллекция фильмов пуста.")
                else:
                    print("Введите имя файла для сохранения")
                    filemame = input()
                    write_CSV(filemame,collection)

            elif mode == 10:
                run_program = False
                
            else:
                print("Такой комманды нет")
                print_menu()    

        except Exception as e:
            print(f"Ошибка {e}")
            continue 

    
if __name__ == "__main__":
    main()
