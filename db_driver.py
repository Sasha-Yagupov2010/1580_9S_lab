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
    
    return True
    

def sort(field, reversed=False):

    def sort_key_function(obj):
        nonlocal field
        name, radius, mass, distance, planet_type = obj
        if field=='name':
            return name
        elif field=='radius':
            return radius
        elif field=='mass':
            return mass
        elif field=='distance':
            return distance
        elif field=='planet_type':
            return planet_type

    data = load_db()
    data.sort(key=sort_key_function,reverse=reversed)
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    return True


def save(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    return True

def del_obj(myobject):
    planet_dict = myobject.to_dict()
    data = load_db()
    
    data.remove(planet_dict) 
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    return True

def edit_obj(newobj,myobject):
    planet_dict = newobj.to_dict()
    data = load_db()
    
    flag = False
    for p in data:
        if isinstance(p, dict) and p.get('name') == planet_dict['name']:
            flag = True

    if not flag: 
        print("объект не найден в базе")
        return False

    del_obj(myobject)
    data.append(planet_dict)
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    return True

def show_db():
    data = load_db()
    for i in data:
        print(i)
