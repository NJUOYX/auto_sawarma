from .tasks import Task


class TaskProducer:
    def produce(self):
        return None


class StubTaskProducer(TaskProducer):
    def __init__(self, tasks: list):
        self.tasks = None

    def produce(self):
        ...
