
test:
	pytest --cov=src/unibool --cov-report=xml tests
	python3-coverage report -m --fail-under 90
	python3-coverage html

format:
	isort src
	isort tests
	black src
	black tests
	flake8 src
	pylint src

html:
	brave htmlcov/index.html