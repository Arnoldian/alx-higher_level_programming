#!/usr/bin/python3
"""
Module using class
"""
import json
import csv
import os.path


class Base:
    """class using methods"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method initializes instances"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method lists to JSON string"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method saves obj in file"""
        file_name = "{}.json".format(cls.__name__)
        list_dict = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dict.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dict)

        with open(file_name, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """Method converts JSON str to dict"""
        if not json_string:
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Method creates instance"""
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return (new)

    @classmethod
    def load_from_file(cls):
        """Method for list of instances"""
        file_name = "{}.json".format(cls.__name__)

        if os.path.exists(file_name) is False:
            return []

        with open(file_name, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        listin = []

        for index in range(len(list_cls)):
            listin.append(cls.create(**list_cls[index]))

        return (listin)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method saves CSV file"""
        file_name = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_dict = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dict = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dict[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dict[:])

        with open(file_name, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """Method loads CSV file"""
        file_name = "{}.csv".format(cls.__name__)

        if os.path.exists(file_name) is False:
            return []

        with open(file_name, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for csv_elem in csv_list:
            csv_dict = {}
            for kv in enumerate(csv_elem):
                csv_dict[list_keys[kv[0]]] = int(kv[1])
            matrix.append(csv_dict)

        listin = []

        for index in range(len(matrix)):
            listin.append(cls.create(**matrix[index]))

        return (listin)
