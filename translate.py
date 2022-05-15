from googletrans import Translator
import googletrans

all_lang = googletrans.LANGUAGES
langcodes = dict(map(reversed,all_lang.items()))
print(langcodes)

translator = Translator()

def check_lang(lang):
    if lang in langcodes.values():
        return False
    else:
        return langcodes[lang]

def translate(text, dest_lang = 'en'):
    return translator.translate(text, dest = dest_lang).text

if __name__ == '__main__':
    print(translate('перевод'))