# google_translate.py
"""
Try to use googletrans module's class Translate
"""
from googletrans import Translator
trans = Translator()
print(trans.translate(text='I like you',src='en',dest='pl').text)
print()

translations = ['The quick brown fox','jump over', 'the lazy dog']
for word in translations:
    print(f"{word:<22}-->{trans.translate(text=word, src='en',dest='pl').text}")

"""
out:
Lubię cię

The quick brown fox   -->Szybki brązowy lis
jump over             -->przeskoczyć
the lazy dog          -->leniwy pies
"""

