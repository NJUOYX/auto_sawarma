from dataclasses import dataclass


@dataclass
class Task:
    target_pos: tuple
    shawarma: int
    kibbeh: int
    cola_orange: int
    cola_coke: int
    orange_juice: int


class TaskQueue:
    def push(self, task):
        ...

    def pop(self):
        ...
