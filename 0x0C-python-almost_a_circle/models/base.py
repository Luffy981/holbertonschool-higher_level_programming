#!/usr/bin/python3
"""Class"""


import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON string representation of list_dictionaries
        -list_dictionaries is a list of dictionaries
        -If list_dictionaries is None or empty, return the string: "[]"
        -Otherwise, return the JSON string representation of list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        JSON string representation of list_objs to a file
        -list_objs is a list of instances who inherits of Base
        -If list_objs is None, save an empty list
        -The filename must be: <Class name>.json - example: Rectangle.json
        -You must use the static method to_json_string (created before)
        -You must overwrite the file if it already exists
        """
        filename = cls.__name__ + ".json"
        result = []
        if list_objs:
            for objs in list_objs:
                dictionary = objs.to_dictionary()
                result.append(dictionary)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(result))

    @staticmethod
    def from_json_string(json_string):
        """
        List of the JSON string representation json_string
        -json_string is a string representing a list of dictionaries
        -If json_string is None or empty, return an empty list
        -Otherwise, return the list represented by json_string
        """
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        -Create a Rectangle or Square instance with “dummy” 
        -Call update instance method to this “dummy”
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy



