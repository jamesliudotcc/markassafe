VENV = env
PYTHON = $(VENV)/bin/python3.10
UVICORN = $(VENV)/bin/uvicorn


run: requirements.checksum $(VENV)/bin/activate
	$(UVICORN) app.main:app

requirements.checksum: requirements.txt $(VENV)/bin/activate
	$(VENV)/bin/pip-sync
	tar -cf - $VENV | md5sum > requirements.checksum

requirements.txt: requirements.in
	$(VENV)/bin/pip-compile -v

$(VENV)/bin/activate:
	python3.10 -m venv env
	$(VENV)/bin/pip install pip-tools

lint: requirements.checksum $(VENV)/bin/activate
	$(VENV)/bin/ruff .
	$(VENV)/bin/ruff format .
	$(VENV)/bin/mypy .

test: requirements.checksum $(VENV)/bin/activate
	$(VENV)/bin/pytest .

.PHONY: run lint test
