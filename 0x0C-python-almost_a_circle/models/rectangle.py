#!/usr/bin/python3
"""rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle inherithed from Base Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    def area(self):
        """Returns the area of the square"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for n in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if len(args) != 0:
            try:
                self.id = args[0]
            except IndexError:
                pass
            try:
                self.__width = args[1]
            except IndexError:
                pass
            try:
                self.__height = args[2]
            except IndexError:
                pass
            try:
                self.__x = args[3]
            except IndexError:
                pass
            try:
                self.__y = args[4]
            except IndexError:
                pass
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        slf_dic = {}
        slf_dic["id"] = self.id
        slf_dic["width"] = self.__width
        slf_dic["height"] = self.__height  # por que aca si se puede priv?
        slf_dic["x"] = self.__x  # por que false r1==r2 task 13
        slf_dic["y"] = self.__y
        return slf_dic

    def __str__(self):
        """String method"""
        return "[Rectangle] ({}) {}/{} - " "{}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    # ----------------------------------------------------------------------------
    # getters and setters
    @property
    def width(self):
        """WIDTH - getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """WIDTH - setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """HEIGHT - getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """HEIGHT - setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """X - getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """X - setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Y - getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """Y - setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
