import logging

from .monitor import Monitor
from .timming import wait
from .tasks import TaskQueue
from .task_consumer import TaskConsumer
from .task_producer import TaskProducer


class Bot:
    def __init__(self, conf: dict):
        self.monitor = Monitor(conf)
        self.__dict__.update(conf)

    def start(self):
        while not self.monitor.stat_game_running:
            wait(1)
        logging.info("GAME START")
        task_queue = TaskQueue()
        task_producer = TaskProducer()
        task_consumer = TaskConsumer()
        while not self.monitor.stat_game_end:
            task_queue.push(task_producer.produce())
            task_consumer.consume(task_queue.pop())
            wait(5)

        logging.info("GAME END")
