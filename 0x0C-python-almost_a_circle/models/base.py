#!/usr/bin/python3
""" module base (Parent class)"""


import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):

        """using JSON data representation"""

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert list_dictionaries to data interchange format JSON"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write JSON of list_object to a file"""
        json_file = cls.__name__ + ".json"
        with open(json_file, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from base"""
        ins_begin = cls.__name__ + ".json"
        ins_final = []
        try:
            with open(ins_begin, "r", encoding="utf-8") as file:
                json_str = file.read()
                obj_list = cls.from_json_string(json_str)
                for objects in obj_list:
                    ins_final.append(cls.create(**objects))
        except FileNotFoundError:
            pass
        return ins_final
