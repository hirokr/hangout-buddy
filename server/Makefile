# Define tools
PYTHON := python
PIP := pip

# Install development dependencies
dev:
	$(PIP) install -r requirements/dev.txt

# Install production dependencies
prod:
	$(PIP) install -r requirements/prod.txt

# Run FastAPI server
run:
	uvicorn hangout_buddy.main:app --reload

# Run tests
test:
	pytest

# Run coverage report
coverage:
	pytest --cov=hangout_buddy --cov-report=html

# Code formatting and linting
lint:
	black . && isort . && flake8

# Clean compiled files and cache
clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
	rm -rf .pytest_cache htmlcov
