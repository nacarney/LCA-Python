import unittest
from unittest import TestCase


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()


class Test(TestCase):
    def test_lca(self):
        self.fail()


class TestNode(TestCase):
    pass


class Test(TestCase):
    def test_tree_to_string(self):
        self.fail()
