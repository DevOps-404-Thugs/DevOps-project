LINTER = flake8
SRC_DIR = source
REQ_DIR = requirements
FRONT_END = front
DOCFILES = $(shell ls *.py | sed -e 's/.py/.html/')

FORCE:

prod: tests coverage github

tests: lint unit

coverage: FORCE
	cd source; coverage report endpoints.py Housings.py Users.py api_config.py test.py; rm .coverage

unit: FORCE
	cd source; coverage run test.py

github: FORCE
	- git commit -a
	git push origin tomroku

lint: FORCE
	$(LINTER) $(SRC_DIR)/endpoints.py $(SRC_DIR)/test.py

dev_env: FORCE
	pip3 install -r requirements.txt

docs: FORCE
	cd source; make docs

travis: lint unit

build_front:
	cd $(FRONT_END); yarn
	cd $(FRONT_END); yarn build