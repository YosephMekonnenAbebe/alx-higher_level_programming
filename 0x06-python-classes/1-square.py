#!/usr/bin/python3
"""Square class definition"""


class Square:
    """A square
    Attributes Representation:
        __size (int): width and lenghth of the square
    """
    def __init__(self, size):
        """Initializes a square class
        Args:
            size (int): width and length of the square
        Returns: None
        """
        self.__size = size
