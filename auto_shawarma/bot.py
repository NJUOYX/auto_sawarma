import logging

from .monitor import Monitor
from .timming import wait
from .tasks import TaskQueue
from .task_consumer import *
from .task_producer import *


class Bot:
    def __init__(self, conf: dict):
        self.monitor = None
        self.consumer = None
        self.producer = None
        self.__dict__.update(conf)

    def start(self):
        monitor = eval(self.monitor)()
        task_queue = TaskQueue()
        task_producer = eval(self.producer)()
        task_consumer = eval(self.consumer)()
        while not self.monitor.stat_game_running:
            wait(1)
        logging.info("GAME START")
        while not monitor.stat_game_end:
            task_queue.push(task_producer.produce())
            task_consumer.consume(task_queue.pop())
            wait(5)

        logging.info("GAME END")
