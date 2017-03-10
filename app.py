import hug
import falcon

from services import yandex_api, microsoft_api, chrome_api

API_MAP = {
    'microsoft': microsoft_api,
    'yandex': yandex_api,
    'google': chrome_api
}

@hug.get('/translate/{service}')
def translate(service: hug.types.text, text: hug.types.text):
    try:
        translator = API_MAP[service]
    except Exception as e:
        raise falcon.HTTPBadRequest('Bad Request', e)

    try:
        return translator(text)
    except Exception as e:
        raise falcon.HTTPInternalServerError('Translate Error', e)

