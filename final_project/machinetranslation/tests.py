import unittest

from translator import english_to_french,french_to_english

class TestEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("hello"),"bonjour")
        self.assertNotEqual(english_to_french("hello"),"merci")

class TestFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(french_to_english("merci"),"hello")

unittest.main()

