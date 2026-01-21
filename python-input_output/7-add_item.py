#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file
"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Проверяем, существует ли файл, чтобы загрузить данные или создать пустой список
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Добавляем все аргументы (пропуская имя самого скрипта)
items.extend(sys.argv[1:])

# Сохраняем обновленный список
save_to_json_file(items, filename)
