import unittest

from pcu_language.pcu_language import detectLanguage

class test_pcu_language(unittest.TestCase):

    def test_detectLanguage(self):
        self.assertEqual(detectLanguage("data/en.txt"), 'en')
        self.assertEqual(detectLanguage("data/fr.txt"), 'fr')

if __name__ == '__main__':
    unittest.main()