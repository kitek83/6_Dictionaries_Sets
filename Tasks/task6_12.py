#task6_12.py
"""
Use the online translator as Google Translate to create translation dictionary
that maps English words to another language.
Display a 2 column table of translations.
"""
from googletrans import Translator

translator = Translator()  #creating the object, which has attribute .translate()
translations = ['The quick brown fox','jump over', 'the lazy dog']

#creating dictionary that maps English word to  translated word:
dict_trans = {}

for word in translations:
    dict_trans[word] = translator.translate(text=word, src='en', dest='de').text  #.text attr gives only translated text

#check dict
print(f'dict_trans: {dict_trans}')

#display a two column table of translations
print()
print(f"{'Word':<25}{'Translation'}")
print(f"{'----':<25}{'-----------'}")

for word, trans in dict_trans.items(): #unpack list of key-value tuples
    print(f'{word:<25}{trans}')

"""
output:
dict_trans: {'The quick brown fox': 'Der schnelle braune Fuchs', 'jump over': 'über etwas springen', 'the lazy dog': 'der faule Hund'}

Word                     Translation
----                     -----------
The quick brown fox      Der schnelle braune Fuchs
jump over                über etwas springen
the lazy dog             der faule Hund

"""