'''
Чтение из БД
Запись в БД
Сортировка БД по выбранному полю
Добавление нового объекта в БД
Удаление объекта из БД
Редактирование объекта в БД
Вывод БД на экран

'''

import json
import os

DB_FILE = "bd.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return []  
    
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.strip():
                data = json.loads(content)
                return data if isinstance(data, list) else []
            else:
                return []
    except json.JSONDecodeError:
        return []

def add_obj(myobject):
    planet_dict = myobject.to_dict()
    data = load_db()
    
    for p in data:
        if isinstance(p, dict) and p.get('name') == planet_dict['name']:
            print(f"Планета '{myobject.name}' уже существует!")
            return False
    
    data.append(planet_dict)
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"Планета '{myobject.name}' успешно добавлена!")
    return True

def sort(field, reversed=False):
    data = load_db()
    
    if not data or field not in data[0]:
        print(f"Поле '{field}' не существует или база данных пуста")
        return False
    
    def sort_key_function(obj):
        return obj.get(field, "")
    
    data.sort(key=sort_key_function, reverse=reversed)
    
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"База данных отсортирована по полю '{field}'")
    return True

def save(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return True

def del_obj(myobject):
    planet_dict = myobject.to_dict()
    data = load_db()
    
    for i, p in enumerate(data):
        if isinstance(p, dict) and p.get('name') == planet_dict['name']:
            del data[i]
            with open(DB_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"Планета '{myobject.name}' успешно удалена!")
            return True
    
    print(f"Планета '{myobject.name}' не найдена в базе данных")
    return False

def edit_obj(newobj, oldobj):
    new_dict = newobj.to_dict()
    old_dict = oldobj.to_dict()
    data = load_db()
    
    found = False
    for i, p in enumerate(data):
        if isinstance(p, dict) and p.get('name') == old_dict['name']:
            found = True
            # Заменяем старый объект на новый
            data[i] = new_dict
            break
    
    if not found:
        print(f"Объект '{oldobj.name}' не найден в базе")
        return False
    
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"Планета '{oldobj.name}' успешно изменена на '{newobj.name}'!")
    return True

def show_db():
    data = load_db()
    if not data:
        print("База данных пуста")
        return
    
    print("\n=== База данных планет ===")
    for i, planet in enumerate(data, 1):
        print(f"\nПланета #{i}:")
        for key, value in planet.items():
            print(f"  {key}: {value}")
    print("==========================\n")

def get_object(name):
    data = load_db()
    
    for p in data:
        if p.get('name') == name:
            return p
    
    print(f"Объект с именем '{name}' не найден")
    return None