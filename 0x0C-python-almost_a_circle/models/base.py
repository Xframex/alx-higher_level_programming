#!/usr/bin/python3
"""Module base"""


import json


class Base:
    """Base comment"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializator for Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries:"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file:"""
        file_name = cls.__name__ + ".json"
        dic_list = []   # list of dictionary reprenstation of an instance
        if list_objs is not None:
            for obj in list_objs:
                dic_list.append(cls.to_dictionary(obj))
        js_str = cls.to_json_string(dic_list)
        with open(file_name, "w", encoding="utf-8") as j_file:
            j_file.write(js_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            list_of_json = []
        else:
            list_of_json = json.loads(json_string)
        return list_of_json

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set:"""
        if cls.__name__ == "Rectangle":
            dummy_obj = cls(10, 10)    # por que no funciona
            dummy_obj.update(**dictionary)  # con el nombre de la clase?
        elif cls.__name__ == "Square":
            dummy_obj = cls(10)
            dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file_name = cls.__name__ + ".json"
        finall_list = []
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                json_str = file.read()
                obj_list = cls.from_json_string(json_str)
                for objects in obj_list:
                    finall_list.append(cls.create(**objects))
        except FileNotFoundError:
            pass
        return (finall_list)
