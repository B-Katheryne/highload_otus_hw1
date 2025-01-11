BLACK := black ./ 
RUFF := ruff check --fix --exit-non-zero-on-fix ./
FLAKE8 := flake8 --statistics ./
PYLINT := pylint ./src
PYTEST := pytest -vv -rP --diff-width=666 -n 6 ./tests/ && date +"%T"

MIGRATION_NAME := migration name

format:
	$(BLACK)

ruff:
	$(RUFF)

lint:
	$(FLAKE8) && $(PYLINT)

test:
	$(PYTEST)

style:
	$(BLACK) && $(RUFF) && $(FLAKE8) && $(PYLINT)

full:
	$(BLACK) && $(RUFF) && $(FLAKE8) && $(PYLINT) && $(PYTEST)

install:
	pip install -r requirements.txt -r requirements_dev.txt -r requirements_test.txt

migrate:
	alembic upgrade head

#make add-migration MIGRATION_NAME="название для миграции"
add-migration:
	alembic revision --autogenerate -m $(MIGRATION_NAME)