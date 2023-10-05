help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-cache - remove cache artifacts"
	@echo "install-dev - install development dependencies"
	@echo "lint - lint code"
	@echo "test - run test suite"


clean: clean-build

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

clean-cache:
	rm -rf .cache/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .pytype/
	rm -rf .coverage
	rm -rf .coverage.*
	rm -rf .tox/
	find  . ! -path "./venv/*" -type d -name ".ipynb_checkpoints"  -exec rm -r {} +
	find  . ! -path "./venv/*" -type d -name "__pycache__"  -exec rm -r {} +

install-dev:
	python3 -m poetry install --with dev,test

lint:
	python3 -m pylint aineko_style

test:
	python3 -m tox
