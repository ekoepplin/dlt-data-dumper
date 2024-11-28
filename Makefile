.PHONY: install run test lint clean full-refresh fix help logs-clean

# Python executable
PYTHON = python3

# Main script
SCRIPT = newsapi_pipeline.py

# Find Python files
PY_FILES = $(shell find . -name "*.py")

# Install dependencies
install:
	pipenv install --dev

# Run the pipeline normally
run:
	$(PYTHON) $(SCRIPT)

# Run in test mode with DuckDB
test:
	$(PYTHON) $(SCRIPT) --test

# Run with full refresh
full-refresh:
	$(PYTHON) $(SCRIPT) --full-refresh

# Run with debug logging
debug:
	$(PYTHON) $(SCRIPT) --log-level DEBUG

# Install linting tools
install-lint:
	pipenv install black flake8 isort autopep8

# Check code style without fixing
lint: install-lint
	-black --check $(PY_FILES)
	-flake8 $(PY_FILES)
	-isort --check $(PY_FILES)
	@echo "Run 'make fix' to automatically fix formatting issues"

# Automatically fix code style issues
fix: install-lint
	black .
	isort .
	find . -type f -name "*.py" -exec autopep8 --in-place --aggressive --aggressive --max-line-length 86 {} +

# Clean generated files
clean:
	rm -rf .dlt
	rm -rf newsapi_data
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

# Clean log files
logs-clean:
	find . -type f -name "*.log" -delete

# Help command
help:
	@echo "Available commands:"
	@echo "  make install       - Install dependencies"
	@echo "  make run           - Run the pipeline"
	@echo "  make test          - Run in test mode with DuckDB"
	@echo "  make full-refresh  - Run with full refresh"
	@echo "  make debug         - Run with debug logging"
	@echo "  make lint          - Run code formatters and linters"
	@echo "  make fix           - Automatically fix code style issues"
	@echo "  make clean         - Clean generated files"
	@echo "  make logs-clean    - Clean up log files"