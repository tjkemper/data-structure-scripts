init:
	pip3 install virtualenv; \
	virtualenv -p `which python3` venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt --editable . 

test:
	. venv/bin/activate; \
	py.test tests/
