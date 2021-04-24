install:
	python -m pip install --upgrade pip &&\
	    pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C valid_phone_number_format.py

test:
	python -m pytest -v --cov=valid_phone_number_format test_valid_phone_number_format.py

all: install lint test
