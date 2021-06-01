import unittest
import reverse

class TestCase(unittest.TestCase):

    def test1(self):
        self.assertEqual(reverse.rev("my name is megan black"), "black megan is name my")
    def test2(self):
        self.assertEqual(reverse.rev("hello world"), "world hello")
    def test3(self): #this will fail
        self.assertEqual(reverse.rev(["hello", "world"]), "world hello")


if __name__ == '__main__':
    unittest.main()