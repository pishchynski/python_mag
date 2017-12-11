import unittest

from event_manager import EventManager


class EventManagerTest(unittest.TestCase):
    def runTest(self):
        manager = EventManager(["./pkgs/"])
        for i in xrange(30):
            manager.notify()


if __name__ == "__main__":
    unittest.main()
