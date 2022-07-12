import unittest

from translator import english_to_french, french_to_english

class TestTranslator_e2f(unittest.TestCase):
    def english_to_french(self):
        self.assertNotEqual(english_to_french("None"), '')
        self.assertNotEqual(english_to_french(0), 0)
        self.assertEqual(english_to_french('Thank you'), 'Je vous remercie')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestTranslator_f2e(unittest.TestCase):
    def french_to_english(self):
        self.assertNotEqual(french_to_english("None"), '')
        self.assertNotEqual(french_to_english(0), 0)
        self.assertEqual(french_to_english('Je vous remercie'), 'Thank you')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()