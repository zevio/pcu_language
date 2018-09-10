# pcu_language
Language detection component (langdetect) for PCU project.
From the path of a text file, detect the main language/all languages used within the text.

Based on [langdetect][langdetect].

[Check PCU project][pcu].

[langdetect]:https://pypi.org/project/langdetect/
[pcu]: https://github.com/zevio/pcu_core

----

## Installation

To install requirements, go to pcu_language/ directory and execute the Makefile with the following command line :

`make init`

# Usage in another project

If you wish to import this module in another Python project, please install it :

`pip install pcu-language`

Then, add this import line at the beginning of your Python file :

`from pcu_langage import pcu_language`

You can now use pcu_language's functions, for example :

`pcu_language.detectLanguage("path/to/txt/file")`

## Test

To test your installation, go to pcu_language/ directory and execute the Makefile with the following command line : 

`make test`
