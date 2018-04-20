#===============================================================================#
#Title           :test_blue                                                     #
#Description     :Unit test to test virtual assistant code                      #
#Author          :joostenstomek@gmail.com                                       #
#Date            :16/04/2018                                                    #
#Version         :1.0.0                                                         #
#Usage           :Python                                                        #
#Python version  :3.6                                                           #
#===============================================================================#

import unittest
from ResponseHandler import Response




##
## @brief      Class for test core functions.
##
class TestCoreFunctions(unittest.TestCase):
	def setUp(self):
		self.url_valid = 'http://api.openweathermap.org/data/2.5/weather?q=Merchtem&APPID=9f5834ee3f9f42f1671bc72b4626f9e7&units=metric'
		self.url_invalid = 'http://api.openwegfgathermap.org/data/2.5/weather?q=Merchtem&APPID=9f5834ee3f9f42f1671bc72b4626f9e7&units=metric'




	def test_url(self):
		r_valid = Response(self.url_valid)
		r_invalid = Response(self.url_invalid)

		self.assertTrue(Response(r_valid.status))
		self.assertTrue(Response(r_invalid.status))

	def test_querry(self):
		r_valid = Response(self.url_valid)
		r_invalid = Response(self.url_invalid)

		self.assertNotEqual(r_valid.json, 'RAW_QUERRY_ERROR') #Querry is valid
		self.assertEqual(r_invalid.json, 'RAW_QUERRY_ERROR') #Querry is invalid
	




		


if __name__ == '__main__':
	unittest.main()