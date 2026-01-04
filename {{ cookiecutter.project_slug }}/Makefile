# Makefile
# =========================================
# Project: {{ cookiecutter.project_name }}
# =========================================

# --------------------------------------------------
# Environment Settings
# --------------------------------------------------
SHELL := /bin/bash
.SHELLFLAGS := -O globstar -c
# --------------------------------------------------
# Build Directories
# --------------------------------------------------
SRC_DIR := src
TEST_DIR := tests
SPHINX_DIR = docs/sphinx
JEKYLL_DIR = docs/jekyll

SPHINX_BUILD_DIR = $(SPHINX_DIR)/_build/html
JEKYLL_OUTPUT_DIR = $(JEKYLL_DIR)/sphinx
# --------------------------------------------------
# Python / Virtual Environment
# --------------------------------------------------
PYTHON := python3
VENV_DIR = .venv
# --------------------------------------------------
# Python Dependencies
# --------------------------------------------------
DEPS := .
DEV_DEPS := .[dev]
DEV_DOCS := .[docs]
# --------------------------------------------------
# Python Commands
# --------------------------------------------------
CREATE_VENV := $(PYTHON) -m venv $(VENV_DIR)
ACTIVATE = source $(VENV_DIR)/bin/activate
PIP := $(ACTIVATE) && $(PYTHON) -m pip
# --------------------------------------------------
# Typing
# --------------------------------------------------
MYPY := $(ACTIVATE) && $(PYTHON) -m mypy
# --------------------------------------------------
# Linting
# --------------------------------------------------
RUFF := $(ACTIVATE) && $(PYTHON) -m ruff
YAMLLINT := $(ACTIVATE) && $(PYTHON) -m yamllint
JINJA := $(ACTIVATE) && jinja2 --strict
# --------------------------------------------------
# Testing
# --------------------------------------------------
PYTEST := $(ACTIVATE) && $(PYTHON) -m pytest
# --------------------------------------------------
# Documentation (Sphinx + Jekyll)
# --------------------------------------------------
SPHINX := $(ACTIVATE) && $(PYTHON) -m sphinx -b markdown
JEKYLL_BUILD := bundle exec jekyll build
JEKYLL_CLEAN := bundle exec jekyll clean
JEKYLL_SERVE := bundle exec jekyll serve

# --------------------------------------------------
# {{ cookiecutter.package_name }} command
# --------------------------------------------------
{{ cookiecutter.package_name|upper }} := $(ACTIVATE) && $(PYTHON) -m {{ cookiecutter.package_name }}.{{ cookiecutter.package_name }}

# -------------------------------------------------------------------
.PHONY: all venv install ruff-lint-check ruff-lint-fix yaml-lint-check \
	jinja2-lint-check lint-check typecheck test docs jekyll-serve clean help

# --------------------------------------------------
# Default: run lint, typecheck, tests, and docs
# --------------------------------------------------
all: install lint-check typecheck test docs

# --------------------------------------------------
# Virtual Environment Setup
# --------------------------------------------------
venv:
	@echo "🔨️ Creating virtual environment..."
	$(CREATE_VENV)
	@echo "✅ Virtual environment created."

install: venv
	@echo "📦 Installing project dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install -e $(DEPS)
	$(PIP) install -e $(DEV_DEPS)
	$(PIP) install -e $(DEV_DOCS)
	@echo "✅ Dependencies installed."

# --------------------------------------------------
# Linting (ruff, yaml, jinja2)
# --------------------------------------------------
ruff-lint-check:
	@echo "🔍 Running ruff linting..."
	$(RUFF) check $(SRC_DIR) $(TEST_DIR)

ruff-lint-fix:
	@echo "🎨 Running ruff lint fixes..."
	$(RUFF) check --show-files $(SRC_DIR) $(TEST_DIR)
	$(RUFF) check --fix $(SRC_DIR) $(TEST_DIR)

yaml-lint-check:
	@echo "🔍 Running yamllint..."
	$(YAMLLINT) .

jinja2-lint-check:
	@echo "🔍 jinja2 linting all template files under {{ cookiecutter.package_name }}..."
	jq '{cookiecutter: .}' cookiecutter.json > /tmp/_cc_wrapped.json
	find '{{ cookiecutter.package_name }}' -type f \
		! -path "{{ cookiecutter.package_name }}/.github/*" \
		! -name "*.png" \
		! -name "*.jpg" \
		! -name "*.ico" \
		! -name "*.gif" \
		-print0 | while IFS= read -r -d '' f; do \
			if file "$$f" | grep -q text; then \
				echo "Checking $$f"; \
				$(JINJA) "$$f" /tmp/_cc_wrapped.json || exit 1; \
			fi; \
		done

lint-check: ruff-lint-check yaml-lint-check jinja2-lint-check

# --------------------------------------------------
# Typechecking (MyPy)
# --------------------------------------------------
typecheck:
	@echo "🧠 Type checking with MyPy..."
	$(MYPY) $(SRC_DIR) $(TESTS_DIR)

# --------------------------------------------------
# Testing (pytest)
# --------------------------------------------------
test:
	@echo "🧪 Running tests with pytest..."
	$(PYTEST) -v --maxfail=1 --disable-warnings $(TEST_DIR)

# --------------------------------------------------
# Documentation (Sphinx + Jekyll)
# --------------------------------------------------
docs:
	@echo "🔨 Building Sphinx documentation as Markdown..."
	$(SPHINX) $(SPHINX_DIR) $(JEKYLL_OUTPUT_DIR)
	@echo "✅ Sphinx Markdown build complete!"
	@echo "🔨 Building Jekyll site..."
	cd $(JEKYLL_DIR) && $(JEKYLL_BUILD)
	@echo "✅ Full documentation build complete!"

jekyll-serve: docs
	@echo "🚀 Starting Jekyll development server..."
	cd $(JEKYLL_DIR) && $(JEKYLL_SERVE)


# --------------------------------------------------
# Run {{ cookiecutter.package_name }} program
# --------------------------------------------------
run:
	@echo "⚙️ running {{ cookiecutter.package_name }}..."
	$({{ cookiecutter.package_name|upper }})

# --------------------------------------------------
# Clean artifacts
# --------------------------------------------------
clean:
	@echo "🧹 Clening build artifacts..."
	rm -rf $(SPHINX_DIR)/_build $(JEKYLL_OUTPUT_DIR)
	cd $(JEKYLL_DIR) && $(JEKYLL_CLEAN)
	rm -rf build dist *.egg-info
	find $(SRC_DIR) $(TEST_DIR) -name "__pycache__" -type d -exec rm -rf {} +
	-[ -d "$(VENV_DIR)" ] && rm -r $(VENV_DIR)
	@echo "🧹 Cleaned build artifacts."

# --------------------------------------------------
# Help
# --------------------------------------------------
help:
	@echo "📦 {{ cookiecutter.project_name }} Makefile"
	@echo ""
	@echo "Usage:"
	@echo "  make venv                   Create virtual environment"
	@echo "  make install                Install dependencies"
	@echo "  make ruff-lint-check        Run Ruff linter"
	@echo "  make ruff-lint-fix          Auto-fix lint issues with python ruff"
	@echo "  make yaml-lint-check        Run YAML linter"
	@echo "  make jinja2-lint-check      Run jinja-cmd linter"
	@echo "  make lint-check             Run all project linters (ruff, yaml, & jinja2)"
	@echo "  make typecheck              Run Mypy type checking"
	@echo "  make test                   Run Pytest suite"
	@echo "  make docs                   Build Sphinx + Jekyll documentation"
	@echo "  make run                    Run {{ cookiecutter.package_name }}.py"
	@echo "  make clean                  Clean build artifacts"
	@echo "  make all                    Run install, lint, typecheck, test, and docs"
