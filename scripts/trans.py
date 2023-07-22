import os
import sys
from deep_translator import GoogleTranslator

def translate(content, lang) -> str:
    return GoogleTranslator(source='auto', target=lang).translate(content) 

if __name__ == "__main__":
    content = sys.argv[1]
    lang = "en"
    if len(sys.argv) > 2:
        lang = sys.argv[2]
    print(translate(content, lang))
