LINTER = flake8
SRC_DIR = source
REQ_DIR = requirements
DOCFILES = $(shell ls *.py | sed -e 's/.py/.html/')

FORCE:

prod: tests github

tests: lint unit

unit: FORCE
	echo "we have to write some tests!"

lint: FORCE
	$(LINTER) $(SRC_DIR)/*.py

dev_env: FORCE
	pip3 install -r $(REQ_DIR)/requirements-dev.txt

docs: FORCE
	cd source; make docs