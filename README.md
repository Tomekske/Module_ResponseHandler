# Project 
### Title
	Respone handler module
### Created by
	Joostens Tomek
### Description
	Class to to obtain a JSON response from a server
### Version 
	1.0.0


# Setup
	pip setup.py install


# Test module
### Option 1
	python test_ResponseHandler.py
### Option 2
	python -W ignore test_ResponseHandler.py 


# Example
### Import module
	import ResponseHandler
### Create object, the URL is the only parameter you'll need
	r = ResponseHandler.Response('https://www.googleapis.com/books/v1/volumes?q=isbn:0747532699')
### Print JSON string
	print(r.json)



