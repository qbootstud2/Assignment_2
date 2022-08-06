import random


class GenRandom:
    """ This class contains methods to generate random int and float numbers in a range as defined in an
     ArtConfig object """

    def __init__(self, a: int, b: int) -> None:
        self.__a: int = a
        self.__b: int = b

    @classmethod
    def gen_int_in_range(cls, a: int, b: int) -> int:
        return random.randint(a, b)

    @classmethod
    def gen_float_in_range(cls, a: float, b: float) -> float:
        return round(random.uniform(a, b), 1)
