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