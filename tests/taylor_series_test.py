import unittest
from src.taylor_series import TaylorSeries

class TaylorSeriesTestCase(unittest.TestCase):
    def setUp(self):
        self.taylor_series = TaylorSeries()

    def test_accuracy_on_big_count(self):
        value = 5
        count = 150

        expected_result = 148.413
        result = round(self.taylor_series.exponential_function(value, count), 3)
        self.assertEqual(result, expected_result, "Bad accuracy for big count")

    def test_accuracy_on_small_count(self):
        value = 5
        count = 15

        expected_result = 148
        result = round(self.taylor_series.exponential_function(value, count), 0)
        self.assertEqual(result, expected_result, "Bad accuracy for small count")

    def test_wrong_count_exception(self):
        value = 5
        count = -1
        self.assertRaises(Exception, self.taylor_series.exponential_function(value, count))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TaylorSeriesTestCase('test_accuracy_on_big_count'))
    suite.addTest(TaylorSeriesTestCase('test_accuracy_on_small_count'))
    suite.addTest(TaylorSeriesTestCase('test_wrong_count_exception'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())