from yandex_translate import YandexTranslate
from mstranslator import Translator
import goslate

from envparse import env
env.read_envfile('keys')


def yandex_api(original_text):
    translate = YandexTranslate(env('YANDEX_KEY'))
    return translate.translate(original_text, 'ru-en')['text'].pop()


#def google_api(original_text):
    #from google.cloud import translate
    #client = translate.Client()
    #return client.translate([original_text], source_language='ru', target_language='en')


def microsoft_api(original_text):
    translator = Translator(env('MSFT_TRANSLATOR'))
    return translator.translate(original_text, lang_from='ru', lang_to='en')


def chrome_api(original_text):
    gs = goslate.Goslate()
    return gs.translate(original_text, 'en', 'ru')
