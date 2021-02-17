# Name : SUYASHI SINGHAL
# Roll No : 2019478
# Group : 9
import unittest
from a1 import changeBase
# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):
	
	def test_change_base(self):
                #CornerCase1
		self.assertTrue(changeBase(700, "EUR", "EUR", "2010-01-12")==700.0)
		#Cornercase2
		self.assertTrue(changeBase(0,"HKD","EUR","2015-04-15")==0)
		self.assertNotAlmostEqual(changeBase(0,"HKD","EUR","2015-04-15"),0.00034552,5)
		self.assertAlmostEqual(changeBase(0,"HKD","EUR","2015-04-15"),0.00034552,3)
		self.assertEqual(changeBase(0,"HKD","EUR","2015-04-15"),0)
                #CornerCase3
		self.assertEqual(changeBase(900, "CAD", "CAD", "2015-12-09"), 900.0)
		self.assertTrue(changeBase(900, "CAD", "CAD", "2015-12-09")==900)
		self.assertNotAlmostEqual(changeBase(100, "CAD", "CAD", "2010-01-12"), 100.005, 3)
                #CornerCase4
		self.assertAlmostEqual(changeBase(50, "USD", "PLN", "2019-10-11"),194.95,delta = 0.1)
		self.assertFalse(changeBase(50, "USD", "PLN", "2019-10-11") == 224.908)
                #CornerCase5
		self.assertFalse(changeBase(57,"HKD","EUR","2013-02-10")==34.32342)
		self.assertAlmostEqual(changeBase(57,"HKD","EUR","2013-02-10"), 5.49540603, delta=0.1)
		#6
		self.assertFalse(changeBase(1, "INR", "GBP", "2010-10-25") == 2.57)
		#7
		self.assertAlmostEqual(changeBase(100, "EUR", "INR", "2010-01-12"), 6620.9999999, delta=0.1)
		#8
		self.assertEqual(changeBase(1, "INR", "GBP", "2010-10-25"), 0.0143404563)
		self.assertAlmostEqual(changeBase(1, "INR", "GBP", "2010-10-25"), 0.0143, delta = 0.1)
		#9
		self.assertTrue(changeBase(250, "USD", "NZD", "2019-10-11") == 394.344833825)
		self.assertEqual(changeBase(250, "USD", "NZD", "2019-10-11"),394.344833825)
		#self.assertEqual(changeBase(1, "INR", "GBP", "2010-10-25"), 2.57)
		#self.assertAlmostEqual(changeBase(1, "INR", "GBP", "2010-10-25"), 2.57, delta = 0.1)
		# these are just sample values. You have to add testcases (and edit these) for various dates.
		# (don't use the current date as the json would keep changing every 4 minutes)
		# you have to hard-code the 2nd parameter of assertEquals by calculating it manually
		# on a particular date and checking whether your changeBase function returns the same
		# value or not.

if __name__=='__main__':
	unittest.main()
