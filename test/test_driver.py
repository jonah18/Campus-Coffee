import unittest
from test.order_test import order_suite


def run_tests(test_suites):
    """Run all tests"""
    test_runner = unittest.TextTestRunner(verbosity=2)
    for test in test_suites:
        test_runner.run(test)


if __name__ == '__main__':
    # Test suites
    test_suites = [order_suite()]
    run_tests(test_suites)
