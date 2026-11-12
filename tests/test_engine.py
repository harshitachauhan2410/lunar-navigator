import unittest
from tools.engine import elev

class TestElevation(unittest.TestCase):
    def test_overhead(self):
        self.assertAlmostEqual(elev(0, 0, 0, 0), 90, places=3)
    def test_opposite_side(self):
        self.assertAlmostEqual(elev(0, 180, 0, 0), -90, places=3)
    def test_pole_sees_horizon(self):
        self.assertAlmostEqual(elev(90, 0, 0, 0), 0, places=3)

if __name__ == '__main__':
    unittest.main()