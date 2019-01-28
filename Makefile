ALFRED_TARGET="${HOME}/Library/Application Support/Alfred 3/Alfred.alfredpreferences/workflows/alfred-worklog"
ALFRED_SRC="$(shell pwd)/alfred-workflow"
BITBAR_PLUGINS=$(shell defaults read com.matryer.BitBar pluginsDirectory)

install: install-alfred install-bitbar

.venv:
	@echo Building virtual env
	@pipenv --venv || pipenv install

install-alfred: .venv
	/usr/bin/install "$(shell pipenv  --venv)/bin/worklog.alfred" alfred-workflow/worklog.alfred
	/usr/bin/install "$(shell pipenv  --venv)/bin/open.alfred" alfred-workflow/open.alfred
	@echo Linking Alfred
	@/bin/ln -his ${ALFRED_SRC} ${ALFRED_TARGET}

install-bitbar: .venv
	@echo Linking Bitbar
	/bin/ln -is "$(shell pipenv  --venv)/bin/worklog.bitbar" "${BITBAR_PLUGINS}/worklog.5m.py"
