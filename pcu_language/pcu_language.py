from langdetect import DetectorFactory 
from langdetect import detect
from langdetect import detect_langs

DetectorFactory.seed = 0 # for more accuracy when several languages are used in a text

def detectLanguage(path):
	"""Return the main language of a text file.
	Parameter :
	path -- path to a text file
	"""
	try:
		file = open(path, "r") # read file
	except IOError:
		print('cannot open', path)
	else:
		language = detect(file.read()) # automatically detect main language of a file from its textual content
		file.close() # close file
	return language

def detectLanguages(path):
	"""Return all languages detected within a text file and associated probabilities for them to be the main language of the text.
	Parameter :
	path -- path to a text file
	"""	
	try:
		file = open(path, "r") # read file
	except IOError:
		print('cannot open', path)
	else:
		languages = detect_langs(file.read()) # automatically detect main language of a file from its textual content
		file.close() # close file
	return languages
