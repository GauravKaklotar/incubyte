import unittest
from Chandrayaan_3 import Chandrayaan

class TestChandrayaan(unittest.TestCase):

    # Passed Test Cases
    def test_Chandrayaan1(self):
        obj = Chandrayaan(0, 0, 0, "N")
        commands = ["f", "u", "u", "d", "u", "f"]
        for command in commands:
            obj.execute_command(command)
        self.assertEqual((obj.x, obj.y, obj.z), (0, 2, 0))
        self.assertEqual(obj.direction, "N")


    def test_Chandrayaan2(self):
        obj = Chandrayaan(1, 0, 2, "N")
        commands = ["u", "r", "l", "f", "f"]
        for command in commands:
            obj.execute_command(command)
        self.assertEqual((obj.x, obj.y, obj.z), (1, 2, 2))
        self.assertEqual(obj.direction, "N")

    def test_Chandrayaan3(self):
        obj = Chandrayaan(0, 1, -2, "Down")
        commands = ["d"]
        for command in commands:
            obj.execute_command(command)
        self.assertEqual(obj.direction, "W")
    
    def test_Chandrayaan4(self):
        obj = Chandrayaan(0, 0, 0, "N")
        commands = ["f", "r", "u", "b", "l"]
        for command in commands:
            obj.execute_command(command)
        self.assertEqual(obj.direction, "W")
        self.assertEqual((obj.x, obj.y, obj.z), (0, 1, -1))

    
    # Failed Test Cases
    def test_Chandrayaan5(self):
        obj = Chandrayaan(0, 1, 0, "W")
        commands = ["d", "f", "b", "l", "r", "u"]
        for command in commands:
            obj.execute_command(command)
        self.assertEqual((obj.x, obj.y, obj.z), (0, 1, 0))
        self.assertEqual(obj.direction, "W")

if __name__ == "__main__":
    unittest.main()
