# Project 
### Title
	Weather
### Created by
	Joostens Tomek
### Description
	Class to to obtain a JSON response from a server

# Download modules
	pip install requests
	pip install httplib2

# Module usage
### 1. Download module 
	git clone https://github.com/Tomekske/Module_ResponseHandler
### 2. Extract project
### 3. Move ResonseHandler.py script to your project location
### 4. Move test_ResonseHandler.py script to your project location

# Test module
### Option 1
	python test_ResponseHandler.py
### Option 2
	python -W ignore test_ResponseHandler.py 

# Example
### Import module
	from ResponseHandler import Response
### Create object, the URL is the only parameter you'll need
	r = Response('https://www.googleapis.com/books/v1/volumes?q=isbn:0747532699')
### Print JSON string
	print(r.json)



