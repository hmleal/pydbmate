help:
	@echo 'Makefile for pydbmate project'

test:
	@PYDBMATE_BASE_DIR="/tmp/db/migrations" pytest

clean:
	@rm -Rf build/
	@rm -Rf dist/
