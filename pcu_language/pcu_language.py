from langdetect import DetectorFactory 
from langdetect import detect
from langdetect import detect_langs

"""
Copyright (C) 2018 Stella Zevio
stella.zevio@lipn.univ-paris13.fr

This program is free software: you can redistribute it and/or modify 
it under the terms of the GNU General Public License as published by 
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
"""

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
