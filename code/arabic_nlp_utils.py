### Miscellaneous utility functions for preprocessing and normalizing Arabic text for NLP purposes.

'''
References:
https://github.com/ahmedaljazzar/arabic-nlp   (Ahmed Jazzar)
https://maximromanov.github.io/2013/01-02.html
https://www.moustaphacheikh.com/2017/11/17/preprocessing  
'''

import re


TATWEEL_UNICODE = '\u0640'
DIACRITICS_REGEX = re.compile(r'[\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652]')
SHADDA_UNICODE = '\u0651'   ##U+0651

ARABIC_CHARS_REGEX = re.compile(r'[\u0621\u0622\u0623\u0624\u0625\u0626\u0627\u0628\u0629\u062A\u062B\u062C\u062D\u062E\u062F\u0630\u0631\u0632\u0633\u0634\u0635\u0636\u0637\u0638\u0639\u063A\u0640\u0641\u0642\u0643\u0644\u0645\u0646\u0647\u0648\u0649\u064A]')

NON_ARABIC_CHARS_REGEX = re.compile(r'[^\u0621\u0622\u0623\u0624\u0625\u0626\u0627\u0628\u0629\u062A\u062B\u062C\u062D\u062E\u062F\u0630\u0631\u0632\u0633\u0634\u0635\u0636\u0637\u0638\u0639\u063A\u0640\u0641\u0642\u0643\u0644\u0645\u0646\u0647\u0648\u0649\u064A]')

ALIFS_REGEX = re.compile(r'[إأٱآ]')
HAMZAS_REGEX = re.compile(r'[ؤئ]')
ALIF_MAKSURA_REGEX = re.compile(r'[ى]')
HA_MARBUTA_REGEX = re.compile(r'[ه]')


def remove_tatweel(text):
    """
    The Tatweel (elongation) is used to stretch words to indicate
    prominence or simply to force vertical justification.
    This symbol has no effect on the meaning of the word so it's
    usually normalized.

    Examples:
        - A word without Tatweel:       جميل
        - The same word with Tatweel:   جـــمـــيـــل
    :param text: The text that we need to extract the Tatweel from.
    :return: A text without Tatweels.
    """
    if text is None:
        return None

    return text.replace(TATWEEL_UNICODE, '')

def remove_diacritics(string):
    return re.sub(DIACRITICS_REGEX, '', string)

def normalize_arabic_letters(string):
    '''orthographic normalization of commonly mis-written arabic letters'''
    string = re.sub(ALIFS_REGEX, 'ا', string)    # different forms of alef
    string = re.sub("ى", "ي", string)            # ya and alef maksoura are often confused
    string = re.sub(HAMZAS_REGEX, 'ء', string)   # different forms of hamza
    #string = re.sub("ه", "ة", string)           # ERROR: THIS REGEX MATCHES HA CHARACTER IN GENERAL!! 
    return string

# Letter removals
def normalize_arabic_text_1(text):
    text = remove_tatweel(text)
    text = remove_diacritics(text)
    return text

# Letter replacements
def normalize_arabic_text_2(text, norm_alif=True, norm_hamza=True, norm_yah=True, norm_tah=True):
    if norm_alif:
        text = re.sub(ALIFS_REGEX, 'ا', text)    # different forms of alef
    if norm_hamza:
        text = re.sub(HAMZAS_REGEX, 'ء', text)   # different forms of hamza
    if norm_yah:
        text = re.sub(ALIF_MAKSURA_REGEX, "ي", text)  # ya and alef maksoura are often confused
    if norm_tah:
        text = re.sub(HA_MARBUTA_REGEX, "ة", text)    # ha and ta marbouta are often confused
    return text


# unit test

if False:
    my_string = ' .'.join(["بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيمِ" ,  " ؤ ئ إ أ ٱ آ واسى في" , 'جـــمـــيـــل' , "مواڞفات وسعر هاتف أيفون 8  ڞ الجديد"])

    print ("Unit test of normalize_arabic_text_*")
    print("")
    print("Raw text:\n",my_string)
    string2 = re.sub(NON_ARABIC_CHARS_REGEX,' ', my_string)
    print("After replacing non-Arabic letters with space:\n",string2)
    string3 = normalize_arabic_text_1(string2)
    print("After removing tatweel and diacritics:\n",string3)
    string4 = normalize_arabic_text_2(string3)
    print("After orthographic letter normalization:\n",string4)

# unit test
if False:
    my_string = "مواڞفات وسعر هاتف أيفون 8  ڞ الجديد"
    print(my_string)
    u = re.findall(NON_ARABIC_CHARS_REGEX,my_string)
    print("  contains", len(u), "non-arabic letters.")
    print('  they are:',' '.join(u))


# unit test
if False:
    string = "بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيمِ"
    print("Before: ",string)
    string = remove_diacritics(string)
    print("After: ",string)


