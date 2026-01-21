#!/usr/bin/python3
"""
Module task_02_csv
Contains a function to convert CSV data to JSON format
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it to a JSON file
    Args:
        csv_filename (str): The name of the source CSV file
    Returns:
        bool: True if successful, False if an error occurred
    """
    try:
        data_list = []
        
        # 1. Читаем CSV и превращаем в список словарей
        with open(csv_filename, mode="r", encoding="utf-8") as csv_f:
            reader = csv.DictReader(csv_f)
            for row in reader:
                data_list.append(row)
        
        # 2. Сериализуем список в JSON файл
        with open("data.json", mode="w", encoding="utf-8") as json_f:
            json.dump(data_list, json_f)
            
        return True
        
    except FileNotFoundError:
        return False
    except Exception:
        return False
