Простой  REST сервис перевода из нескольких API.

Выбор сервиса перевода указывается в path у URL, например `/translate/{service}`.

Сейчас доступны `/transalte/yandex` и `/translate/microsoft`.

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

# Проврека

Кириллические символы надо закодировать. Браузер делает это автоматически. 
В curl надо закодировать (--data-urlencode) и присоединить к URL (-G опция).

```curl -vs 'localhost:8000/translate/yandex' -G --data-urlencode 'text=привет мир'```

```curl -vs 'localhost:8000/translate/microsoft' -G --data-urlencode 'text=привет мир'```

 Не работает.
```curl -vs 'localhost:8000/translate/google' -G --data-urlencode 'text=привет мир'```


# Ключи

## Yandex
Получение ключа
https://tech.yandex.ru/keys/get/?service=trnsl


## Google

Сгенерировать ключ для service account в json формате:

https://cloud.google.com/storage/docs/authentication#generating-a-private-key
http://google-cloud-python.readthedocs.io/en/latest/google-cloud-auth.html

Полученный ключ записать в переменную окружения.
`export GOOGLE_APPLICATION_CREDENTIALS="google-key.json"`

Оплатить $20.
https://cloud.google.com/translate/pricing?csw=1


## Microsoft
Инструкция по ссылке. Ключ начниает рабоатть не сразу.
https://github.com/wronglink/mstranslator#usage