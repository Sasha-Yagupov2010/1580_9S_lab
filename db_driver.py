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
        print("Файл не существует!")
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


def save(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return True
