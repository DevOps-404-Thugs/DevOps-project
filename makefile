LINTER = flake8
SRC_DIR = source
REQ_DIR = requirements
FRONT_END = front
DOCFILES = $(shell ls *.py | sed -e 's/.py/.html/')

FORCE:

prod: tests

tests: lint unit

unit: FORCE
	cd source; coverage run test.py; coverage report endpoints.py

github: FORCE
	- git commit -a
	git push origin master

lint: FORCE
	$(LINTER) $(SRC_DIR)/endpoints.py $(SRC_DIR)/test.py

dev_env: FORCE
	pip3 install -r $(REQ_DIR)/requirements-dev.txt
	cd $(FRONT_END); npm install
	cat $(FRONT_END)/requirements-npm.txt | xargs npm install -g

docs: FORCE
	cd source; make docs

travis: tests