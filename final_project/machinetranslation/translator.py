"""this module translates english to french or vice versa"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """takes in english and translate to french"""

    french_text_translate = MyMemoryTranslator(source='english', 
    target='french').translate(english_text)
    return french_text_translate

def french_to_english(french_text):
    """ takes in french and translates to english"""

    english_text_translate = MyMemoryTranslator(source='french', 
    target='english').translate(french_text)
    return english_text_translate
