PYTHON           ?= python
PIP              ?= $(PYTHON) -m pip
COVERAGE         ?= coverage
PYCODESTYLE      ?= pycodestyle
FLAKE8           ?= flake8
GUNICORN         ?= gunicorn
PRECOMMIT        ?= pre-commit
ANSIBLE_LINT     ?= ansible-lint


help: Makefile
	@echo
	@echo " Choose a command run in Pilgrim:"
	@echo
	@sed -n 's/^##//p' $< | column -t -s ':' |  sed -e 's/^/ /'
	@echo


## config: Install dependencies.
.PHONY: config
config:
	$(PIP) install -r requirements.test.txt
	$(PIP) install -r requirements.txt


## lint-pycodestyle: PyCode Style Lint
.PHONY: lint-pycodestyle
lint-pycodestyle:
	@echo "\n>> ============= Pycodestyle Linting ============= <<"
	@find app -type f -name \*.py | while read file; do echo "$$file" && $(PYCODESTYLE) --config=./pycodestyle --first "$$file" || exit 1; done


## lint-flake8: Flake8 Lint.
.PHONY: lint-flake8
lint-flake8:
	@echo "\n>> ============= Flake8 Linting ============= <<"
	@find app -type f -name \*.py | while read file; do echo "$$file" && $(FLAKE8) --config=flake8.ini "$$file" || exit 1; done


## lint: Lint The Code.
.PHONY: lint
lint: lint-pycodestyle lint-flake8
	@echo "\n>> ============= All linting cases passed! ============= <<"


## test: Run Test Cases.
.PHONY: test
test:
	@echo "\n>> ============= Run Test Cases ============= <<"
	$(PYTHON) manage.py test


## migration: Create DB Migration Files.
.PHONY: migration
migration:
	@echo "\n>> ============= Make Migrations ============= <<"
	$(PYTHON) manage.py makemigrations


## migrate: Migrate Database.
.PHONY: migrate
migrate:
	@echo "\n>> ============= Migrate ============= <<"
	$(PYTHON) manage.py migrate


## run: Run Server.
.PHONY: run
run:
	@echo "\n>> ============= Run Server ============= <<"
	$(GUNICORN) --bind 0.0.0.0:8000 app.wsgi


## coverage: Get test coverage.
.PHONY: coverage
coverage:
	@echo "\n>> ============= Get test coverage ============= <<"
	$(COVERAGE) run --source='app' manage.py test app
	$(COVERAGE) report -m
	$(COVERAGE) html


## create-env: Create .env file.
.PHONY: create-env
create-env:
	@echo "\n>> ============= Create .env file ============= <<"
	cp .env.example .env


## makemessages: Make translation files.
.PHONY: makemessages
makemessages:
	@echo "\n>> ============= Make translation files ============= <<"
	$(PYTHON) manage.py makemessages


## rqstats: Get the worker stats
.PHONY: rqstats
rqstats:
	@echo "\n>> ============= Get Worker Stats ============= <<"
	$(PYTHON) manage.py rqstats --interval=1


## worker: Run the worker
.PHONY: worker
worker:
	@echo "\n>> ============= Run Worker ============= <<"
	$(PYTHON) manage.py rqworker default


## outdated-pkg: Show outdated python packages
.PHONY: outdated-pkg
outdated-pkg:
	@echo "\n>> ============= List Outdated Packages ============= <<"
	$(PIP) list --outdated


## precommit: Run pre-commit hooks
.PHONY: precommit
precommit:
	$(PRECOMMIT) install
	$(PRECOMMIT) run --all-files


## lint_plans: Lint ansible plans
.PHONY: lint_plans
lint_plans:
	$(ANSIBLE_LINT) -p plan


## ci: Run all CI tests.
.PHONY: ci
ci: coverage lint lint_plans precommit outdated-pkg
	@echo "\n>> ============= All quality checks passed ============= <<"


.PHONY: help
