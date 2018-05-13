ALFRED_TARGET="${HOME}/Library/Application Support/Alfred 3/Alfred.alfredpreferences/workflows/alfred-worklog"
ALFRED_SRC="$(shell pwd)/alfred-workflow"
BITBAR_PLUGINS=$(shell defaults read com.matryer.BitBar pluginsDirectory)
VIRTUAL_ENV:="$(shell pwd)/.venv"

refresh: .venv
	@echo Installing scripts
	@.venv/bin/pip install -e .

install: install-alfred install-bitbar

.venv:
	@echo Building virtual envw
	python3 -m venv .venv

install-alfred: refresh
	/bin/cp "${VIRTUAL_ENV}/bin/worklog.alfred" alfred-workflow/worklog.alfred
	/bin/cp "${VIRTUAL_ENV}/bin/open.alfred" alfred-workflow/open.alfred
	@echo Linking Alfred
	@/bin/ln -his ${ALFRED_SRC} ${ALFRED_TARGET}

install-bitbar: refresh
	@echo Linking Bitbar
	/bin/ln -is "${VIRTUAL_ENV}/bin/worklog.bitbar" "${BITBAR_PLUGINS}/worklog.5m.py"
