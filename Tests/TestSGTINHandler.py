import unittest
from Implementation.SGTINHandler import SGTINHandler


class TestSGTINHandler(unittest.TestCase):

    def setUp(self):
        self.handler = SGTINHandler()

    def tearDown(self):
        pass

    def test_urn_sgtin_input(self):
        test_str = "urn:epc:id:sgtin:0614141.100013.3"
        expected_human_readable = "(01)10614141000132(21)3"

        actual_converted_str = self.handler.to_human_readable(test_str)
        self.assertEqual(expected_human_readable, actual_converted_str)

    def test_human_readable_input(self):
        test_str = "(01)10614141000132(21)3"
        expected_human_readable = "(01)10614141000132(21)3"

        actual_converted_str = self.handler.to_human_readable(test_str)
        self.assertEqual(expected_human_readable, actual_converted_str)

    def test_custom_input(self):
        test_str = "level:10614141000132.Sn:3"
        expected_human_readable = "(01)10614141000132(21)3"

        actual_converted_str = self.handler.to_human_readable(test_str)
        self.assertEqual(expected_human_readable, actual_converted_str)