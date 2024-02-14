#!/usr/bin/python3
"""
Module - base.py
"""
import json


class Base():
    """
    class Base for Almost a Circle project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class Base constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        class_name = "{}.json".format(cls.__name__)
        list_dict = []
        if list_objs is None:
            pass
        else:
            for objects in list_objs:
                list_dict.append(objects.to_dictionary())
        with open(class_name, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set, creating
        a 'dummy' instance beforehand
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        file_name = "{}.json".format(cls.__name__)
        try:
            with open(file_name, "r") as f:
                json_string = f.read()
        except Exception as e:
            return []
        list_inst = []
        inst_dict_list = cls.from_json_string(json_string)
        for i in inst_dict_list:
            list_inst.append(cls.create(**i))
        return list_inst
