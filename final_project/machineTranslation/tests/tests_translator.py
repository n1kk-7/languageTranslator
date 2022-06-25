import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

import unittest
from translate import english_to_french, french_to_english

class TranslationTest(unittest.TestCase):
    def test_Null_Value_for_EtF(self):
        self.assertEqual(english_to_french(None), 'Please type something to convert.')
    
    def test_Hi_Value_for_EtF(self):
        self.assertNotEqual(english_to_french('Hi'), 'Hi')

    def test_Hello(self):
        self.assertEqual(english_to_french("Hello"), 'Bonjour')

    def test_Null_Value_for_FtE(self):
        self.assertEqual(french_to_english(None), 'Please type something to convert.')
    
    def test_Salut_Value_for_FtE(self):
        self.assertNotEqual(french_to_english('Salut'), 'Salut')

    def test_Bonjour(self):
        self.assertEqual(french_to_english("Bonjour"), 'Hello')

if __name__ == '__main__':
    unittest.main()