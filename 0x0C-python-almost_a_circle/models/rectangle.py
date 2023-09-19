#!/usr/bin/python3
"""rectangle"""


from models.base import Base


class Rectangle(Base):

    """Rectangle inherithed from Base Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor of class"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    """Getters and setters """

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        return "Rectangle({}, {}, {}, {}, {})".format(
            self.width, self.height, self.x, self.y, self.id
        )

    def area(self):
        return self.width * self.height

    def display(self):
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }

    """area function of rectangle"""

    def area(self):
        return self.__width * self.__height

    """print the character (#) in stdout """
    """or draw a rectangle """

    def display(self):
        for n in range(self.y):
            print()
        for m in range(self.height):
            print(" " * self.x + "#" * self.width)

    """str method to represent as astring"""

    def __str__(self):
        return "Rectangle({}, {}, {}, {}, {})".format(
            self.width, self.height, self.x, self.y, self.id
        )

    """argument/key value behaviour to each attribute"""

    def update(self, *args, **kwargs):
        if args:
            num_args = len(args)
            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.width = args[1]
            if num_args >= 3:
                self.height = args[2]
            if num_args >= 4:
                self.x = args[3]
            if num_args >= 5:
                self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    """Rectangle instance to dictionary representation"""

    def to_dictionary(self):

        rec_dic = {}
        rec_dic["id"] = self.id
        rec_dic["width"] = self.__width
        rec_dic["height"] = self.__height
        rec_dic["x"] = self.__x
        rec_dic["y"] = self.__y
        return rec_dic
