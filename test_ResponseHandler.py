#===============================================================================#
#Title           :Unit test ResponseHandler                                     #
#Description     :Unit test to test Response class                              #
#Author          :joostenstomek@gmail.com                                       #
#Date            :20/04/2018                                                    #
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
		self.url_valid = 'https://www.googleapis.com/books/v1/volumes?q=isbn:0747532699'
		self.url_invalid = 'https://www.googbhbjhleapis.com/books/v1/volumes?q=isbn:0747532699'



	##
	## @brief     Method to determintate wether url is valid or invallid
	##
	def test_url(self):
		r_valid = Response(self.url_valid)
		r_invalid = Response(self.url_invalid)

		self.assertTrue(Response(r_valid.status))
		self.assertTrue(Response(r_invalid.status))



	##
	## @brief     Method to determintate wether querry is valid or invallid
	##
	def test_querry(self):
		r_valid = Response(self.url_valid)
		r_invalid = Response(self.url_invalid)

		self.assertNotEqual(r_valid.json, 'RAW_QUERRY_ERROR') #Querry is valid
		self.assertEqual(r_invalid.json, 'RAW_QUERRY_ERROR') #Querry is invalid

	

if __name__ == '__main__':
	unittest.main()