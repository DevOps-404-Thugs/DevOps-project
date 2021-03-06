LINTER = flake8
SRC_DIR = source
REQ_DIR = requirements
FRONT_END = front
DOCFILES = $(shell ls *.py | sed -e 's/.py/.html/')

FORCE:

coverage_back:
	cd source; coverage report endpoints.py Housings.py Users.py api_config.py test.py; rm .coverage

prod: lint unit coverage_back unit_front github

tests: lint unit unit_front

coverage: FORCE
	cd source; coverage report endpoints.py Housings.py Users.py api_config.py test.py; rm .coverage
	cd $(FRONT_END); yarn test --coverage --collectCoverageFrom=src/App.js

unit: FORCE
	cd source; coverage run test.py

unit_front: FORCE
	cd $(FRONT_END); yarn test

github: FORCE
	- git commit -a
	git push origin master

lint: FORCE
	$(LINTER) $(SRC_DIR)/endpoints.py $(SRC_DIR)/test.py

dev_env: FORCE
	pip3 install -r requirements.txt

docs: FORCE
	cd source; make docs

travis: lint unit build_front unit_front

build_front:
	cd $(FRONT_END); yarn
	cd $(FRONT_END); yarn build
