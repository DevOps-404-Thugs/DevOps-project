LINTER = flake8
SRC_DIR = source
REQ_DIR = requirements
DOCFILES = $(shell ls *.py | sed -e 's/.py/.html/')

FORCE:

prod: tests github

tests: lint unit

unit: FORCE
	echo "need to get new unit test for JSON communication"

github: FORCE

lint: FORCE
	$(LINTER) $(SRC_DIR)/endpoints.py

dev_env: FORCE
	pip3 install -r $(REQ_DIR)/requirements-dev.txt

docs: FORCE
	cd source; make docs
