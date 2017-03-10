venv:
	virtualenv ./env/
	. ./env/bin/activate; pip install -r requirements.txt

run:
	. ./env/bin/activate; hug -f app.py

.PHONY: venv run
