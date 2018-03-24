help:
	@echo 'Makefile for pydbmate project'

test:
	@pytest

clean:
	@rm -Rf build/
	@rm -Rf dist/