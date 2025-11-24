# Makefile
# =========================================
# Project: {{ cookiecutter.project_name }}
# =========================================

# --------------------------------------------------
# ⚙️ Environment Settings
# --------------------------------------------------
SHELL := /bin/bash
.SHELLFLAGS := -O globstar -c
# If V is set to '1' or 'y' on the command line,
# AT will be empty (verbose).  Otherwise, AT will
# contain '@' (quiet by default).  The '?' is a
# conditional assignment operator: it only sets V
# if it hasn't been set externally.
V ?= 0
ifeq ($(V),0)
    AT = @
else
    AT =
endif
# Detect if we are running inside GitHub Actions CI.
# GitHub sets the environment variable GITHUB_ACTIONS=true in workflows.
# We set CI=1 if running in GitHub Actions, otherwise CI=0 for local runs.
ifeq ($(GITHUB_ACTIONS),true)
CI := 1
else
CI := 0
endif
# Define a reusable CI-safe runner
define run_ci_safe =
( $1 || [ "$(CI)" != "1" ] )
endef
# --------------------------------------------------
# ⚙️ Build Settings
# --------------------------------------------------
PACKAGE_NAME := {{ cookiecutter.package_name }}
PACKAGE_AUTHOR := "{{ cookiecutter.author }}"
PACKAGE_VERSION := {{ cookiecutter.version }}
# --------------------------------------------------
# 📁 Build Directories
# --------------------------------------------------
SRC_DIR := ./src
TEST_DIR := ./tests
DOCS_DIR := ./docs
SPHINX_DIR := $(DOCS_DIR)/sphinx
JEKYLL_DIR := $(DOCS_DIR)/jekyll

SPHINX_BUILD_DIR := $(SPHINX_DIR)/_build/html
JEKYLL_OUTPUT_DIR := $(JEKYLL_DIR)/sphinx
# --------------------------------------------------
# SUBDIRS (Recursive Make Builds)
# --------------------------------------------------
# TODO: $(SPHINX_DIR)
DOC_SUBDIRS := $(JEKYLL_DIR)
SUBDIRS := $(JEKYLL_DIR)
# --------------------------------------------------
# 🐍 Python / Virtual Environment
# --------------------------------------------------
PYTHON_CMD := python3.11
VENV_DIR := .venv
# --------------------------------------------------
# 🐍 Python Dependencies
# --------------------------------------------------
DEPS := .
DEV_DEPS := .[dev]
DEV_DOCS := .[docs]
# --------------------------------------------------
# 🐍 Python Commands
# --------------------------------------------------
CREATE_VENV := $(PYTHON_CMD) -m venv $(VENV_DIR)
ACTIVATE = source $(VENV_DIR)/bin/activate
PYTHON := $(ACTIVATE) && $(PYTHON_CMD)
PIP := $(PYTHON) -m pip
# --------------------------------------------------
# 🧠 Typing (mypy)
# --------------------------------------------------
MYPY := $(PYTHON) -m mypy
# --------------------------------------------------
# 🔍 Linting (ruff, yaml)
# --------------------------------------------------
RUFF := $(PYTHON) -m ruff
YAMLLINT := $(PYTHON) -m yamllint
# --------------------------------------------------
# 🎨 Formatting (black)
# --------------------------------------------------
BLACK := $(PYTHON) -m black
# --------------------------------------------------
# 🧪 Testing (pytest)
# --------------------------------------------------
PYTEST := $(PYTHON) -m pytest
# --------------------------------------------------
# 📘 Documentation (Sphinx + Jekyll)
# --------------------------------------------------
SPHINX := $(PYTHON) -m sphinx -b markdown
JEKYLL_BUILD := bundle exec jekyll build --quiet
JEKYLL_CLEAN := bundle exec jekyll clean
JEKYLL_SERVE := bundle exec jekyll serve
# --------------------------------------------------
# 🏃‍♂️ {{ cookiecutter.package_name }} command
# --------------------------------------------------
{{ cookiecutter.package_name|upper }} := $(PYTHON) -m {{ cookiecutter.package_name }}.{{ cookiecutter.package_name }}
# -------------------------------------------------------------------
.PHONY: all venv install black-formatter-check black-formatter-fix format-check format-fix \
	ruff-lint-check ruff-lint-fix yaml-lint-check lint-check lint-fix \
	typecheck test sphinx jekyll jekyll-serve readme build-docs run-docs clean help
# --------------------------------------------------
# Default: run lint, typecheck, tests, and build-docs
# --------------------------------------------------
all: install lint-check typecheck test build-docs
# --------------------------------------------------
# Virtual Environment Setup
# --------------------------------------------------
venv:
	$(AT)echo "🐍️ Creating virtual environment..."
	$(AT)$(CREATE_VENV)
	$(AT)echo "✅ Virtual environment created."

install: venv
	$(AT)echo "📦 Installing project dependencies..."
	$(AT)$(PIP) install --upgrade pip
	$(AT)$(PIP) install -e $(DEPS)
	$(AT)$(PIP) install -e $(DEV_DEPS)
	$(AT)$(PIP) install -e $(DEV_DOCS)
	$(AT)echo "✅ Dependencies installed."
# --------------------------------------------------
# Formating (black)
# --------------------------------------------------
black-formatter-check:
	$(AT)echo "🔍 Running black formatter style check..."
	$(AT)$(call run_ci_safe, $(BLACK) --check $(SRC_DIR) $(TESTS_DIR))
	$(AT)echo "✅ Finished formatting check of Python code with Black!"
	
black-formatter-fix:
	$(AT)echo "🎨 Running black formatter fixes..."
	$(AT)$(BLACK) $(SRC_DIR) $(TESTS_DIR)
	$(AT)echo "✅ Finished formatting Python code with Black!"

format-check: black-formatter-check
format-fix: black-formatter-fix
# --------------------------------------------------
# Linting (ruff, yaml)
# --------------------------------------------------
ruff-lint-check:
	$(AT)echo "🔍 Running ruff linting..."
	$(AT)$(RUFF) check $(SRC_DIR) $(TEST_DIR)

ruff-lint-fix:
	$(AT)echo "🎨 Running ruff lint fixes..."
	$(AT)$(RUFF) check --show-files $(SRC_DIR) $(TEST_DIR)
	$(AT)$(RUFF) check --fix $(SRC_DIR) $(TEST_DIR)

yaml-lint-check:
	$(AT)echo "🔍 Running yamllint..."
	$(AT)$(YAMLLINT) .

lint-check: ruff-lint-check yaml-lint-check
lint-fix: ruff-lint-fix
# --------------------------------------------------
# Typechecking (MyPy)
# --------------------------------------------------
typecheck:
	$(AT)echo "🧠 Type checking with MyPy..."
	$(AT)$(call run_ci_safe, $(MYPY) $(SRC_DIR) $(TESTS_DIR))
	$(AT)echo "✅ Python typecheck complete!"
# --------------------------------------------------
# Testing (pytest)
# --------------------------------------------------
test:
	$(AT)echo "🧪 Running tests with pytest..."
	$(AT)$(call run_ci_safe, $(PYTEST) $(TEST_DIR))
	$(AT)echo "✅ Python tests complete!"
# --------------------------------------------------
# Documentation (Sphinx + Jekyll)
# --------------------------------------------------
sphinx:
	$(AT)echo "🔨 Building Sphinx documentation 📘 as Markdown..."
	$(AT)$(SPHINX) $(SPHINX_DIR) $(JEKYLL_OUTPUT_DIR)
	$(AT)echo "✅ Sphinx Markdown build complete!"

jekyll:
	for dir in $(DOC_SUBDIRS); do \
        $(MAKE) -C $$dir all || exit 1; \
    done

readme:
	$(AT)echo "🔨 Building ./README.md 📘 with Jekyll..."
	$(AT)mkdir -p $(README_GEN_DIR)
	$(AT)cp $(JEKYLL_DIR)/_config.yml $(README_GEN_DIR)/_config.yml
	$(AT)cp $(JEKYLL_DIR)/Gemfile $(README_GEN_DIR)/Gemfile
	$(AT)printf "%s\n" "---" \
		"layout: raw" \
		"permalink: /README.md" \
		"---" > $(README_GEN_DIR)/README.md
	$(AT)printf '%s\n' '<!--' \
		'  Auto-generated file. Do not edit directly.' \
		'  Edit $(JEKYLL_DIR)/README.md instead.' \
		'  Run ```make readme``` to regenrate this file' \
		'-->' >> $(README_GEN_DIR)/README.md
	$(AT)cat $(JEKYLL_DIR)/README.md >> $(README_GEN_DIR)/README.md
	$(AT)cd $(README_GEN_DIR) && $(JEKYLL_BUILD)
	$(AT)cp $(README_GEN_DIR)/_site/README.md ./README.md
	$(AT)echo "🧹 Clening README.md build artifacts..."
	$(AT)rm -r $(README_GEN_DIR)
	$(AT)echo "✅ README.md auto generation complete!"

jekyll-serve: docs
	$(AT)echo "🚀 Starting Jekyll development server..."
	$(AT)cd $(JEKYLL_DIR) && $(JEKYLL_SERVE)

build-docs: sphinx jekyll readme
run-docs: jekyll-serve
# --------------------------------------------------
# Run {{ cookiecutter.package_name }} program
# --------------------------------------------------
run:
	$(AT)echo "🏃‍♂️ running {{ cookiecutter.package_name }}..."
	$(AT)$({{ cookiecutter.package_name|upper }})
# --------------------------------------------------
# Clean artifacts
# --------------------------------------------------
clean:
	$(AT)echo "🧹 Clening build artifacts..."
	$(AT)rm -rf $(SPHINX_DIR)/_build $(JEKYLL_OUTPUT_DIR)
	$(AT)$(call run_ci_safe, cd $(JEKYLL_DIR) && $(JEKYLL_CLEAN))
	$(AT)rm -rf build dist *.egg-info
	$(AT)find $(SRC_DIR) $(TEST_DIR) -name "__pycache__" -type d -exec rm -rf {} +
	$(AT)-[ -d "$(VENV_DIR)" ] && rm -r $(VENV_DIR)
	$(AT)echo "🧹 Cleaned build artifacts."
# --------------------------------------------------
# Help
# --------------------------------------------------
help:
	$(AT)echo "📦 $(PACKAGE_NAME) Makefile"
	$(AT)echo ""
	$(AT)echo "Usage:"
	$(AT)echo "  make venv                   Create virtual environment"
	$(AT)echo "  make install                Install dependencies"
	$(AT)echo "  make format-check           Run all project formatter checks (black)"
	$(AT)echo "  make format-fix             Run all project formatter autofixes (black)"
	$(AT)echo "  make ruff-lint-check        Run Ruff linter"
	$(AT)echo "  make ruff-lint-fix          Auto-fix lint issues with python ruff"
	$(AT)echo "  make yaml-lint-check        Run YAML linter"
	$(AT)echo "  make lint-check             Run all project linters (ruff & yaml)"
	$(AT)echo "  make lint-fix               Run all project linter autofixes (ruff)"
	$(AT)echo "  make typecheck              Run Mypy type checking"
	$(AT)echo "  make test                   Run Pytest suite"
	$(AT)echo "  make sphinx                 Generate Sphinx Documentation"
	$(AT)echo "  make jekyll                 Generate Jekyll Documentation"
	$(AT)echo "  make readme                 Uses Jekyll $(JEKYLL_DIR)/README.md for readme generation"
	$(AT)echo "  make build-docs             Build Sphinx + Jekyll documentation"
	$(AT)echo "  make run-docs               Serve Jekyll site locally"
	$(AT)echo "  make run                    Run {{ cookiecutter.package_name }}.py"
	$(AT)echo "  make clean                  Clean build artifacts"
	$(AT)echo "  make all                    Run install, lint, typecheck, test, and docs"
	$(AT)echo "Options:"
	$(AT)echo "  V=1             Enable verbose output (show all commands being executed)"
	$(AT)echo "  make -s         Run completely silently (suppress make's own output AND command echo)"
