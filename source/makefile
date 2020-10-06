DOCFILES = $(shell ls *.py | sed -e 's/.py/.html/')

docs: $(DOCFILES)

%.html: %.py
	pydoc3 -w ./$<
	git add $@
