import unittest

from event_manager import *


class EventManagerTest(unittest.TestCase):
    def runTest(self):
        collector = Collector(["./pkgs/"])
        assert len(collector.actions) == 3
        collector.execute(5)
        collector.execute(10)
        collector.execute(16)


if __name__ == "__main__":
    unittest.main()
