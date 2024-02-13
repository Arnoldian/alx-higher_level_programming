#!/usr/bin/python3
"""
Module using class inhering from another class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class using methods"""

    def __init__(self, size, x=0, y=0, id=None):
        """Method initializing instances"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method for special str"""
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_x_y = "{}/{} - ".format(self.x, self.y)
        str_w_h = "{}/{}".format(self.width, self.height)

        return (str_square + str_id + str_x_y + str_w_h)

    @property
    def size(self):
        """Method getting size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Method setting size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Method for special string"""
        str_rect = "[Square] "
        str_id = "({}) ".format(self.id)
        str_x_y = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return (str_rect + str_id + str_x_y + str_size)

    def update(self, *args, **kwargs):
        """Method for update"""
        if args is not None and len(args) is not 0:
            list_attrs = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_attrs[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Method for dict with attr"""
        list_attrs = ['id', 'size', 'x', 'y']
        res_dict = {}

        for key in list_attrs:
            if key == 'size':
                res_dict[key] = getattr(self, 'width')
            else:
                res_dict[key] = getattr(self, key)

        return (res_dict)
