class Monitor:
    def __init__(self, conf, **kwargs):
        self.conf = conf

    @property
    def stat_game_running(self):
        return False

    @property
    def stat_game_end(self):
        return False
