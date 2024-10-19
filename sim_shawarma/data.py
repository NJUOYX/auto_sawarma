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

    def __init__(self, **kwargs):
        ...


class InteractiveData(Data, ABC):
    @property
    @abstractmethod
    def interact_by_click(self) -> bool:
        ...

    @property
    @abstractmethod
    def interact_by_drag(self) -> bool:
        ...

    @abstractmethod
    def valid_target(self, target: Data) -> bool:
        ...


class Clock(Data):
    secs_limit: int


class Employee(InteractiveData):
    manually: bool

    def register_supply_method(self, name, method):
        self.__dict__[f'supply_{name}'] = method

    def eat_shawarma(self):
        ...

    @property
    def interact_by_click(self) -> bool:
        return True

    @property
    def interact_by_drag(self) -> bool:
        return False

    def valid_target(self, target: Data) -> bool:
        return False


class GameStatus:
    ...
