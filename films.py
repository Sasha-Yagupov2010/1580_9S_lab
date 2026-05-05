# Фильм: Название, режиссер, год, жанр, рейтинг, продолжительность

from database.db_driver import Db_Driver
db = Db_Driver("database/films.json")


class Film:
    _id_counter = 0
    
    def __init__(self, name=None, rezhiser=None,  year=None, score=None, length=None, film_type=None):
        self.name = name
        self.rezhiser = rezhiser
        self.year = year
        self.score = score
        self.length = length
        self.film_type = film_type

        self.__id = Film._id_counter
        Film._id_counter += 1
        print(f"Создание ID {self.__id}")


    def __str__(self):
        return (f"Планета '{self.name}' (ID: {self.__id}): "
                f"Радиус={self.rezhiser} км, Масса={self.year} кг, "
                f"Расстояние={self.score} млн км, Тип='{self.film_type}'")

    def __repr__(self):
        return f"Film(name='{self.name}', rezhiser={self.rezhiser}, year={self.year}, score={self.score}, type='{self.film_type}')"

    def __copy__(self):
        return Film(
            name=self.name,
            rezhiser=self.rezhiser,
            year=self.year,
            score=self.score,
            film_type=self.film_type
        )

    def __del__(self):
        print(f"Удаление ID {self.__id}")

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.score > other.score

    def __le__(self, other):
        return self.score <= other.score

    def __ge__(self, other):
        return self.score >= other.score

    def to_dict(self):
        return {
            "name": self.name,
            "rezhiser": self.rezhiser,
            "year": self.year,
            "score": self.score,
            "length":self.length,
            "film_type": self.film_type,
        }
    
    @staticmethod
    def get_film_types():
        return ["каменная", "газовый гигант", "ледяной гигант"]

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            rezhiser=data.get("rezhiser"),
            year=data.get("year"),
            score=data.get("score"),
            length=data.get("length"),
            film_type=data.get("film_type")
        )


class FilmCollection:
    def __init__(self):
        self.film_array = []

    def load(self):
        try:
            data = db.load_db()
            if data:
                self.film_array = [] 
                self.add_list_films(data)
                return True
            return False
        
        except Exception as e:
            print(f"Ошибка загрузки из БД: {e}")
            return False

    def get_array(self):
        return self.film_array

    def apply(self):
        try:
            data_to_save = []
            for film in self.film_array:
                data_to_save.append(film.to_dict() if isinstance(film, Film) else film)
                    
            return db.save(data_to_save)
        
        except Exception as e:
            print(f"Ошибка сохранения в БД: {e}")
            return False

    def add_film(self, film: Film):
        if not isinstance(film, Film):
            print(f"Ошибка, нельзя добавить объект типа{type(film)}")
            return False
        if film in self.film_array:
            print(f"Ошибка, объект уже существует")
            return False
        self.film_array.append(film)
        return True
    
    def add_list_films(self, arr_):

        for item in arr_:
            if isinstance(item, Film):
                self.add_film(item)

            elif isinstance(item, dict):
                try:
                    film = Film(
                        name=item.get('name', ''),
                        rezhiser=item.get('rezhiser', 0),
                        year=item.get('year', 0),
                        score=item.get('score', 0),
                        film_type=item.get('film_type', '')
                    )
                    self.add_film(film)
                except Exception as e:
                    print(f"Ошибка создания фильма из словаря: {e}")
            else:
                print(f"Неизвестный тип данных: {type(item)}")

    def delete_film(self,film):
        if film in self.film_array:
            self.film_array.remove(film)    
            return True
        
        print("Объект не найден в базе!")
        return False

    def get_count(self):
        return len(self.film_array)
    

    def check_in_db(self, new_film, exclude_name):
        for p in self.film_array:
            if p.name == new_film.name:
                if exclude_name and p.name == exclude_name:
                    continue 
                print(f"Фильм с названием '{new_film.name}' уже существует!")
                return True
            return False


    def edit_film(self, old_name, new_film):
        for i in range(self.get_count()):
            if self.film_array[i].name == old_name:
                if old_name != new_film.name:

                    if self.check_in_db(new_film, exclude_name=old_name):
                        return False
                
                self.film_array[i] = new_film
                print(f"Фильм '{old_name}' изменен на '{new_film.name}'")
                return True
    
        print(f"Фильм '{old_name}' не найден")
        return False

    def get_film(self, name):
        for film in self.film_array:
            if film.name == name:
                return film
        return None

    def show_all(self):
        for i in self.film_array:
            print(i)


    def clear_all(self):
        self.film_array.clear()


    ''' sort '''

    def sort_film(self, field_key="score", reverse=False):
        
        n = len(self.film_array)
        for i in range(n):
            for j in range(0, n-i-1):
                film1 = self.film_array[j]
                film2 = self.film_array[j+1]
                
   
                if field_key == "name":
                    need_swap = film1.name > film2.name
                elif field_key == "rezhiser":
                    need_swap = film1.rezhiser > film2.rezhiser
                elif field_key == "year":
                    need_swap = film1.year > film2.year
                elif field_key == "score":
                    need_swap = film1.score > film2.score
                elif field_key == "length":
                    need_swap = film1.length > film2.length  
                elif field_key == "film_type":
                    need_swap = film1.film_type > film2.film_type
                else:
                    print(f"Неизвестное поле для сортировки: '{field_key}'. Сортирую по рейтингу")
                    need_swap = film1.score > film2.score
                
                if reverse:
                    need_swap = not need_swap
                
                if need_swap:
                    self.film_array[j], self.film_array[j+1] = self.film_array[j+1], self.film_array[j]
        
        return True

