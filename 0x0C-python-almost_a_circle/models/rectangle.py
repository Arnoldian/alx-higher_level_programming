#!/usr/bin/python3
"""
Module using class
"""
from models.base import Base


class Rectangle(Base):
    """class using methods"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Method initializing instances"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Method getting width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Method setting width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Method getting height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Method setting height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Method getting x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Method setting x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Method getting y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Method setting y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area of the rectangle object """
        return (self.width * self.height)

    def display(self):
        """ displays a rectangle """
        rect = self.y * "\n"
        for i in range(self.height):
            rect += (" " * self.x)
            rect += ("#" * self.width) + "\n"

        print(rect, end='')

    def __str__(self):
        """Mehtod for special str"""
        str_rect = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_x_y = "{}/{} - ".format(self.x, self.y)
        str_w_h = "{}/{}".format(self.width, self.height)

        return (str_rect + str_id + str_x_y + str_w_h)

    def update(self, *args, **kwargs):
        """Method for update"""
        if args is not None and len(args) is not 0:
            list_attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Method for dict with properties"""
        list_attrs = ['id', 'width', 'height', 'x', 'y']
        res_dict = {}

        for key in list_attrs:
            res_dict[key] = getattr(self, key)

        return (res_dict)
