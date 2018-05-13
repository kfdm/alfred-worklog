ALFRED_TARGET="${HOME}/Library/Application Support/Alfred 3/Alfred.alfredpreferences/workflows/alfred-worklog"
ALFRED_SRC="$(shell pwd)/alfred-workflow"

install: install-alfred


.venv:
	python3 -m venv .venv
	.venv/bin/pip install -e .


install-alfred:
	@echo Installing scripts
	.venv/bin/pip install --upgrade --no-deps --install-option="--install-scripts=${ALFRED_SRC}" .['alfred']
	#@echo Linking Alfred
	#/bin/ln -s ${ALFRED_SRC} ${ALFRED_TARGET}

clean:
	/bin/rm alfred-workflow/open.py
	/bin/rm alfred-workflow/worklog.py
