from Logging import Logger
import unittest


# run: python3 -m unittest Logging_Test.py 
class LoggerTest(unittest.TestCase):
    def test_Creation(self):
        # test if logging works
        x = Logger()
        x.Debug('Test')
        x.Info('Test')
        x.Warning('Test')   
        self.assertIsNotNone(x)

if __name__ == '__main__':
    unittest.main()