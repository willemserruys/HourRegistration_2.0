from DADataBaseConnection import DADataBaseConnection
import unittest


# run: python3 -m unittest DADataBaseConnection_Test.py 
class DADataBaseConnectionTest(unittest.TestCase):
    def test_Creation(self):
        # test if class is a singleton
        x = DADataBaseConnection()
        y = DADataBaseConnection()
        print(x)
        print(y)
        
        self.assertEqual(x,y)

    def test_Config(self):
        x = DADataBaseConnection()
        self.assertEqual(x.Name,'HourRegistration.db')

if __name__ == '__main__':
    unittest.main()