#!/usr/bin/python3
"""
Module task_00_basic_serialization
Contains functions for basic JSON serialization and deserialization
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file
    Args:
        data (dict): Python dictionary to serialize
        filename (str): Name of the output JSON file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Deserializes a JSON file to recreate a Python dictionary
    Args:
        filename (str): Name of the input JSON file
    Returns:
        dict: The deserialized Python dictionary
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
