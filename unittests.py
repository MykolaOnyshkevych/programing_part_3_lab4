from main import count_elements_in_string
import unittest
class TestGraph(unittest.TestCase):

    def setUp(self) -> None:
        self.first_numb = "101101101"
        self.second_numb = 5

        self.third_numb = '1111101'
        self.forth_numb = 5

        self.fifth_numb = '100111011110100100111110110011100101000111100101110010001100111011110100100111110110011100101000110010110000111100101110010001'
        self.sixth_numb = 7

        self.first_result = 3
        self.second_result = 1
        self.third_result = 5

    def test_first_list_from_example(self):
        self.assertEqual(count_elements_in_string(self.first_numb, self.second_numb),
                         self.first_result)

    def test_second_list_from_example(self):
        self.assertEqual(count_elements_in_string(self.third_numb, self.forth_numb),
                         self.second_result)

    def test_third_list_from_example(self):
        self.assertEqual(count_elements_in_string(self.fifth_numb, self.sixth_numb),
                         self.third_result)

