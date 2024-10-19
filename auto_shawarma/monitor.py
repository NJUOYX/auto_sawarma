class Monitor:
    def __init__(self, *args, **kwargs):
        ...

    @property
    def stat_game_running(self):
        return False

    @property
    def stat_game_end(self):
        return False


class StubMonitor(Monitor):
    ...
