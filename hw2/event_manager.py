from collector import Collector

class EventManager:
    def __init__(self, packages):
        self.index = 0
        self.collector = Collector(packages)

    def notify(self):
        try:
            self.collector.collect()
        except Exception as e:
            raise e

        self.index += 1
