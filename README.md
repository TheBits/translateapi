Простой  REST сервис перевода из нескольких API.

Выбор сервиса перевода происходит автоматически. Пример `/translate/?lang=<lang>&text=<text>`.

Сейчас доступны Yandex, Microsoft и Transltr.

# Запуск

Следует подготовить файл `keys` с ключами для сервисов.
Формат файла:

```
YANDEX_KEY="<trnsl.1.1....>"
MSFT_TRANSLATOR="<hash>"
```

Команды для запуска сервиса:

```
make venv
make run
```

# Проверка

Кириллические символы надо закодировать. Браузер делает это автоматически. 
В curl надо закодировать (--data-urlencode) и присоединить к URL (-G опция).

```curl -vs 'localhost:8000/translate/?lang=bg' -G --data-urlencode 'text=Съешь ещё этих мягких французских булок, да выпей же чаю.'```

Вернёт
```
{"translator": "YandexTranslator", "text": "Яжте повече от тези меки френски ролца, да имат същия чай."}
```

Языки для которых будет выбран Microsoft Translation API.
{'to', 'fil', 'cy', 'hi', 'th', 'bs-Latn', 'zh-CHT', 'ht', 'fj', 'mg', 'sr-Cyrl', 'vi', 'he', 'sr-Latn', 'otq', 'af', 'ms', 'sm', 'ty', 'mt', 'ar', 'ko', 'tlh', 'yue', 'zh-CHS', 'tlh-Qaak', 'mww', 'ja', 'sw', 'id', 'fa', 'ur', 'yua'}

```curl -vs 'localhost:8000/translate/?lang=bg' -G --data-urlencode 'text=Съешь ещё этих мягких французских булок, да выпей же чаю.'```

Вернёт
```
{"translator": "MicrosoftTranslator", "text": "Bwyta mwy o hyn rholiau Ffrangeg meddal, oes Mae un te."}
```

# Ключи

## Yandex
Получение ключа
https://tech.yandex.ru/keys/get/?service=trnsl


## Microsoft
Инструкция по ссылке. Ключ начинает работать не сразу.
https://github.com/wronglink/mstranslator#usage