import unittest

from model import Map


class ModelTest(unittest.TestCase):
    def runTest(self):
        size = [10, 5]
        self.assertEqual(5, len(Map.generate_map(size)))

        ocean_test = Map('config.json')
        self.assertEqual(False, ocean_test.check_prey(0, 0))
        self.assertEqual(False, ocean_test.check_predator(1, 1))
        self.assertEqual(True, ocean_test.check_move(ocean_test.predators[0], 0))


if __name__ == "__main__":
    unittest.main()
