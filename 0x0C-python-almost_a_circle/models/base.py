#!/usr/bin/python3
"""Class"""


import json
import csv
import turtle


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
            return []
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

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        result = []
        try:
            with open(filename, encoding="utf-8") as file:
                obj_list = cls.from_json_string(file.read())
                for dictionary in obj_list:
                    result.append(cls.create(**dictionary))
                return result
        except:
            return result

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Method to serialize in csv
        input: object (you can have the information with dict)
        result: [[4, 5, 0, 0], [5, 7, 9, 1]]
        """
        list_rectangle = ["id", "width", "height", "x", "y"]
        list_square = ["id", "size", "x", "y"]
        filename = cls.__name__ + ".csv"
        result = []

        if list_objs:
            for objs in list_objs:
                # First recollect the info of the object with a dict
                dictionary = objs.to_dictionary()
                middle_result = []
                # second obtein the values in a ordered class list
                if cls.__name__ == "Rectangle":
                    for item in list_rectangle:
                        middle_result.append(dictionary[item])
                if cls.__name__ == "Square":
                    for item in list_square:
                        middle_result.append(dictionary[item])
                # append the list to result list
                result.append(middle_result)
        with open(filename, "w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(result)

    @classmethod
    def load_from_file_csv(cls):
        """
        Method to  deserialize in CSV
        -input: ['1', '10', '7', '2', '8']
        -first: your need to create a dictionary of the instance
        -{'width': '10', 'height': '7', 'id': '1', 'x': '2', 'y': '8'}
        -second: you need to create an object from the dict
        -Return: [140462163445632] [Square] (5) 0/0 - 5
        """
        list_rectangle = ["id", "with", "height", "x", "y"]
        list_square = ["id", "size", "x", "y"]
        filename = cls.__name__ + ".csv"
        result = []

        try:
            with open(filename, encoding="utf-8") as file:
                obj_list = csv.reader(file)
                # read obj_list < csv.reader object
                if cls.__name__ == "Rectangle":
                    for list in obj_list:
                        # create dictionary
                        dict = {}
                        for key, value in zip(list_rectangle, list):
                            dict[key] = int(value)
                        # create an object and append to a list
                        result.append(cls.create(**dict))
                if cls.__name__ == "Square":
                    for list in obj_list:
                        # create dictionary
                        dict = {}
                        for key, value in zip(list_square, list):
                            dict[key] = int(value)
                        # create an object and append to a list
                        result.append(cls.create(**dict))
                return result
        except:
            return result

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        kael = turtle.Turtle()
        kael.speed(3)
        wn = turtle.Screen()
        wn.bgcolor("#00897B")

        def set_position(x, y):
            kael.penup()
            kael.goto(x, y)
            kael.pendown()

        def create_rectangle(width, height, kael):
            kael.begin_fill()
            for i in range(2):
                kael.forward(width)
                kael.right(90)
                kael.forward(height)
                kael.right(90)
            kael.end_fill()

        for rectangle in list_rectangles:
            kael.color("blue")
            set_position(rectangle.x, rectangle.y)
            create_rectangle(rectangle.width, rectangle.height, kael)
            set_position(-1 * rectangle.x, -1 * rectangle.y)

        for square in list_squares:
            kael.color("red")
            set_position(square.x, square.y)
            create_rectangle(square.size, square.size, kael)
            set_position(-1 * square.x, -1 * square.y)
        kael.color("black")
        set_position(300, -200)
        kael.write("Luffy", font=("Garamond", 32, "normal"))

        turtle.done()
