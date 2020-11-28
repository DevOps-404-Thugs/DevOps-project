LINTER = flake8
SRC_DIR = source
REQ_DIR = requirements
FRONT_END = front
DOCFILES = $(shell ls *.py | sed -e 's/.py/.html/')

FORCE:

prod: tests github

tests: lint unit

unit: FORCE
	cd source; coverage run test.py; coverage report endpoints.py; rm .coverage

unit1: FORCE
	cd source; python3 test.py

github: FORCE
	- git commit -a
	git push origin tomroku

lint: FORCE
	$(LINTER) $(SRC_DIR)/endpoints.py $(SRC_DIR)/test.py

dev_env: FORCE
	pip3 install -r requirements.txt

docs: FORCE
	cd source; make docs

travis: lint unit1

build_front:
	cd $(FRONT_END); yarn build