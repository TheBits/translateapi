import hug
import requests
import falcon

from yandex_translate import YandexTranslate
from mstranslator import Translator

from envparse import env
env.read_envfile('keys')


class TransltrTranslator(object):
    MAX_TEXT = 100

    def translate(self, text, translate_to):
        payload = {
            "text": text,
            "from": "ru",
            "to": translate_to,
        }
        response = requests.post(
            'http://www.transltr.org/api/translate',
            data=payload,
            headers={'Accept': 'application/json'}
        )
        return response.json()['translationText']

    def languages(self):
        langs = requests.get('http://www.transltr.org/api/getlanguagesfortranslate',
                headers={'Accept': 'application/json'})
        return [item['languageCode'] for item in langs.json()]


class MicrosoftTranslator(object):
    MAX_TEXT = 10000

    def __init__(self):
        self.translator = Translator(env('MSFT_TRANSLATOR'))

    def translate(self, text, translate_to):
        return self.translator.translate(text, lang_from='ru', lang_to=translate_to)

    def languages(self):
        return self.translator.get_langs()


class YandexTranslator(object):
    MAX_TEXT = 10000

    def __init__(self):
        self.translator = YandexTranslate(env('YANDEX_KEY'))

    def translate(self, text, translate_to):
        pair = 'ru-%s' % translate_to
        return self.translator.translate(text, pair)['text'].pop()

    def languages(self):
        return self.translator.langs


def check_availability(translator, text_size, language):
    if translator.MAX_TEXT < text_size:
        return None
    if language not in translator.languages():
        return None
    return translator


# by priority
TRANSLATORS = [
    YandexTranslator(),
    MicrosoftTranslator(),
    TransltrTranslator(),
]


@hug.get('/translate/')
def translate(lang: hug.types.text, text: hug.types.text):
    try:
        available = (check_availability(translator, len(text), lang)
                for translator in TRANSLATORS)
        translator = next(t for t in available if t is not None)
    except StopIteration:
        raise falcon.HTTPBadRequest('Bad Request', 'There is no available translators')
    except Exception as e:
        raise falcon.HTTPBadRequest('Bad Request', e)

    try:
        response = {
            "translator": translator.__class__.__name__,
            "text": translator.translate(text, lang),
        }
        return response
    except Exception as e:
        raise falcon.HTTPInternalServerError('Translate Error', e)
