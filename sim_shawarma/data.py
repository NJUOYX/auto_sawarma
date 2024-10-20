import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass


class Data(ABC):
    def __new__(cls, **kwargs):
        obj = super.__new__(cls)
        for attr, t in cls.__annotations__.items():
            if (av := kwargs.get(attr)) and isinstance(av, t):
                obj.__dict__[attr] = av
            else:
                raise ValueError(f"[INITIALIZATION ERROR]: {cls.__name__} with {kwargs}")
        return obj


class Container(Data):
    volume: int
    contains: int

    @property
    def empty(self):
        return self.contains == 0

    @property
    def full(self):
        return self.volume == self.contains

    def supplied(self) -> bool:
        if self.full:
            return False
        else:
            self.contains += 1
            return True


class Supplier(Data, ABC):
    @abstractmethod
    def supply(self) -> bool:
        ...


class BasicFood(Container, Supplier):
    def supply(self) -> bool:
        if self.empty:
            return False
        else:
            self.contains -= 1
            return True


class Shawarma(Data):
    limit_of_beef: int
    limit_of_cucumber: int
    limit_of_cream: int
    limit_of_fries_potato: int
    limit_of_molasses: int

    def __init__(self, *, limit_of_beef, limit_of_cucumber, limit_of_cream, limit_of_fries_potato, limit_of_molasses):
        self.beef = 0
        self.cucumber = 0
        self.cream = 0
        self.fries_potato = 0
        self.molasses = 0
        self.wrapped = False
        self.packed = False

    def _add_something(self, something: str, num: int) -> bool:
        if (cur_num := getattr(self, something)) and (limit := getattr(self, f'limit_of_{something}')):
            if cur_num + num <= limit:
                setattr(self, something, cur_num + num)
            else:
                return False
        raise ValueError(f"Unexpected adding thing: {something}")

    def add_beef(self, num: int) -> bool:
        return self._add_something('beef', num)

    def add_cucumber(self, num: int) -> bool:
        return self._add_something('cucumber', num)

    def add_cream(self, num: int) -> bool:
        return self._add_something('cream', num)

    def add_fries_potato(self, num: int) -> bool:
        return self._add_something('fries_potato', num)

    def add_molasses(self, num: int) -> bool:
        return self._add_something('molasses', num)

    def pack_it(self) -> bool:
        if self.packed:
            return False
        else:
            self.packed = True
            return True

    def wrapped_it(self) -> bool:
        if self.wrapped:
            return False
        else:
            self.wrapped = True
            return True


class Clock(Data):
    secs_limit: int


class Employee(Data):
    manually: bool

    def eat_shawarma(self, shawarma):
        ...


class GameStatus:
    ...
