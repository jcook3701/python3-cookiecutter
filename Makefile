# Makefile for freecad_stub_generator
# =========================================
# FreeCAD Stub Generator - Makefile
# =========================================
SHELL := /bin/bash

PYTHON := python3
VENV_DIR = .venv
VENV_SYS_DIR = .venv-system

# Paths
SRC_DIR := src
TEST_DIR := tests
SPHINX_DIR = docs/sphinx
JEKYLL_DIR = docs/jekyll
SPHINX_BUILD_DIR = $(SPHINX_DIR)/_build/html
JEKYLL_OUTPUT_DIR = $(JEKYLL_DIR)/sphinx

# dependencies
DEPS := .
DEV_DEPS := .[dev]

# FreeCAD environment variables (previously in .env)
QT_QPA_PLATFORM := offscreen
FREECAD_STUB_GENERATOR := $(HOME)/Documents/git_repo/freecad-stub-generator/freecad_stub_generator/
FREECAD_MOD := /usr/share/freecad/Mod/Web:/usr/share/freecad/Mod/Tux:/usr/share/freecad/Mod/Draft:/usr/share/freecad/Mod/OpenSCAD:/usr/share/freecad/Mod/Import:/usr/share/freecad/Mod/Path:/usr/share/freecad/Mod/Drawing:/usr/share/freecad/Mod/Part:/usr/share/freecad/Mod/Material:/usr/share/freecad/Mod/Points:/usr/share/freecad/Mod/Test:/usr/share/freecad/Mod/Arch:/usr/share/freecad/Mod/Image:/usr/share/freecad/Mod/Robot:/usr/share/freecad/Mod/AddonManager:/usr/share/freecad/Mod/Start:/usr/share/freecad/Mod/Inspection:/usr/share/freecad/Mod/PartDesign:/usr/share/freecad/Mod/ReverseEngineering:/usr/share/freecad/Mod/Fem:/usr/share/freecad/Mod/Surface:/usr/share/freecad/Mod/Sketcher:/usr/share/freecad/Mod/Measure:/usr/share/freecad/Mod/TechDraw:/usr/share/freecad/Mod/Show:/usr/share/freecad/Mod/Spreadsheet:/usr/share/freecad/Mod/Raytracing:/usr/share/freecad/Mod/MeshPart:/usr/share/freecad/Mod/Mesh:/usr/share/freecad/Mod/Idf:/usr/share/freecad/Mod:/usr/lib/freecad/Mod
FREECAD_LIB := /usr/lib/freecad/lib:/usr/lib/freecad-python3/lib
FREECAD_EXT := /usr/share/freecad/Ext
FREECAD_BIN := /usr/lib/freecad/bin
FREECAD_MACRO := $(HOME)/.FreeCAD/Macro:/usr/lib/freecad/Macro


# Python path to include FreeCAD modules
PYTHONPATH := $(FREECAD_STUB_GENERATOR):$(FREECAD_MOD):$(FREECAD_LIB):$(FREECAD_EXT):$(QT_LIB):$(FREECAD_BIN):$(FREECAD_MACRO):$(PYTHONPATH)

# Commands
CREATE_VENV := $(PYTHON) -m venv $(VENV_DIR)
CREATE_VENV_SYS := $(PYTHON) -m venv --system-site-packages $(VENV_SYS_DIR)
ACTIVATE = source $(VENV_DIR)/bin/activate
ACTIVATE_SYS = source $(VENV_SYS_DIR)/bin/activate
PIP := $(ACTIVATE) && $(PYTHON) -m pip
PIP_SYS := $(ACTIVATE_SYS) && $(PYTHON) -m pip
RUFF := $(ACTIVATE) && $(PYTHON) -m ruff
MYPY := $(ACTIVATE) && $(PYTHON) -m mypy
PYTEST := $(ACTIVATE) && $(PYTHON) -m pytest

# -------------------------------------------------------------------
.PHONY: all venv install lint-check lint-fix typecheck test docs jekyll-serve clean help

# Default: run lint, typecheck, tests, and docs
all: lint-check typecheck test docs

# Virtual Environment Setup
venv:
	@echo "Creating virtual environment..."
	$(CREATE_VENV)
	@echo "✅ Virtual environment created."

venv-system:
	@echo "Creating virtual environment with system packages..."
	$(CREATE_VENV_SYS)
	@echo "✅ System venv created."

# Install dev dependencies
install: venv
	@echo "📦 Installing project dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install -e $(DEV_DEPS)
	@echo "✅ Dependencies installed."

install-system: venv-system
	@echo "📦 Installing project dependencies in system venv..."
	$(PIP_SYS) install --upgrade pip
	$(PIP_SYS) install -e $(DEPS)
	@echo "✅ System dependencies installed."

# Lint Check
lint-check: install
	$(RUFF) check $(SRC_DIR) $(TEST_DIR)

# Lint auto-fix
lint-fix: install
	$(RUFF) check --fix --show-files $(SRC_DIR) $(TEST_DIR)

# Type checking
typecheck: install
	$(MYPY) $(SRC_DIR)

# Run tests
test: install
	$(PYTEST) -v --maxfail=1 --disable-warnings $(TEST_DIR)

# Docs: build Sphinx Markdown and copy into Jekyll
docs: install
	@echo "📘 Building Sphinx documentation as Markdown..."
	export PYTHONPATH=$(PYTHONPATH) && \
	$(ACTIVATE) && $(PYTHON) -m sphinx -b markdown $(SPHINX_DIR) $(JEKYLL_OUTPUT_DIR)
	@echo "✅ Sphinx Markdown build complete!"
	@echo "🧱 Building Jekyll site..."
	cd $(JEKYLL_DIR) && bundle exec jekyll build
	@echo "✅ Full documentation build complete!"

jekyll-serve: docs
	@echo "🚀 Starting Jekyll development server..."
	cd $(JEKYLL_DIR) && bundle exec jekyll serve

run: install-system
	export QT_QPA_PLATFORM=$(QT_QPA_PLATFORM) && \
	export PYTHONPATH=$(PYTHONPATH) && \
	$(ACTIVATE_SYS) && $(PYTHON) -m freecad_stub_generator.freecad_stub_generator \
		--stubs-path ./stubs \
	        --freecad \
		--pyside

# Clean build artifacts
clean:
	rm -rf $(SPHINX_DIR)/_build $(JEKYLL_OUTPUT_DIR)
	cd $(JEKYLL_DIR) && bundle exec jekyll clean
	rm -rf build dist *.egg-info
	find $(SRC_DIR) $(TEST_DIR) -name "__pycache__" -type d -exec rm -rf {} +
	-[ -d "$(VENV_DIR)" ] && rm -r $(VENV_DIR)
	-[ -d "$(VENV_SYS_DIR)" ] && rm -r $(VENV_SYS_DIR)
	@echo "🧹 Cleaned build artifacts."

help:
	@echo "📦 freecad_stub_generator Makefile"
	@echo ""
	@echo "Usage:"
	@echo "  make venv        Create virtual environment"
	@echo "  make install     Install dependencies"
	@echo "  make lint-check  Run Ruff linter"
	@echo "  make lint-fix    Auto-fix lint issues"
	@echo "  make typecheck   Run Mypy type checking"
	@echo "  make test        Run Pytest suite"
	@echo "  make docs        Build Sphinx + Jekyll documentation"
	@echo "  make clean       Clean build artifacts"
	@echo "  make run         Run freecad_stub_generator.py"
	@echo "  make all         Run lint, typecheck, test, and docs"
