PIP_BIN := .venv/bin/pip
APP_BIN := .venv/bin/worklog


$(PIP_BIN):
	python3.7 -m venv .venv
	$(PIP_BIN) install --upgrade wheel pip setuptools

pip: $(PIP_BIN)
	$(PIP_BIN) install --upgrade wheel pip setuptools
	
list: $(PIP_BIN)
	$(PIP_BIN) list --outdated

$(APP_BIN): $(PIP_BIN)
