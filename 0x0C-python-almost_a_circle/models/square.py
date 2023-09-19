#!/usr/bin/python3
"""rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """inherited class from Rectanle no DRY (dont repeat your self) !!"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """Getters / Setters from inherited class behaviour"""

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

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
        sqr_dic = {}
        sqr_dic["id"] = self.id
        sqr_dic["size"] = self.width
        sqr_dic["x"] = self.x  # por que false r1==r2 task 13
        sqr_dic["y"] = self.y
        return sqr_dic
