#!/usr/bin/python3
"""
Module task_01_pickle
Contains a class CustomObject that supports pickling
"""
import pickle


class CustomObject:
    """Custom class to demonstrate pickling"""

    def __init__(self, name, age, is_student):
        """Initialize attributes"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object attributes"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance to a file"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load an instance of the class from a file"""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, Exception):
            return None
