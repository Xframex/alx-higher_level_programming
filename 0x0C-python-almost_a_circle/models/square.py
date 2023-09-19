#!/usr/bin/python3
"""square module"""


from models.rectangle import Rectangle

import sys
sys.path.append(r'/alx-higher_level_programming/0x0C-python-almost_a_circle')


class Square(Rectangle):
    """Square class inherited from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square constructor"""
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if len(args) != 0:
            try:
                self.id = args[0]
            except IndexError:
                pass
            try:
                self.width = args[1]
                self.height = args[1]
            except IndexError:
                pass
            try:
                self.x = args[2]
            except IndexError:
                pass
            try:
                self.y = args[3]
            except IndexError:
                pass
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        slf_dic = {}
        slf_dic["id"] = self.id
        slf_dic["size"] = self.width
        slf_dic["x"] = self.x  # por que false r1==r2 task 13
        slf_dic["y"] = self.y
        return slf_dic

    def __str__(self):
        """String mathod"""
        return "[Square] ({}) {}/{} - " "{}".format(
                self.id, self.x, self.y, self.width)

    # getters and setters

    @property
    def size(self):
        """SIZE - getter"""
        return self.width  # Por que no funciona con __width?

    @size.setter
    def size(self, new_size):
        """SIZE - setter"""
        self.width = new_size
        self.height = new_size
