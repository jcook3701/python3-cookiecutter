{% import '.cookiecutter_includes/license/__init__.j2' as license_macros with context %}
{{- license_macros.license_header.create(
  cookiecutter.license,
  cookiecutter.copyright,
  cookiecutter.project_slug,
  file_name='verbose.py',
  comment_style='hash') -}}

from dataclasses import replace
from typing import Any

from nutrimatic.core.logger import setup_logging
from nutrimatic.models import CLIConfig


def verbose_mode(cfg: CLIConfig, verbose: bool) -> Any:
    """
    Handle the --verbose / -v flag.

    Override verbosity if CLI flag provided
    """
    if verbose:
        cfg = replace(cfg, verbose=True)
    logger = setup_logging(cfg)

    logger.debug("Verbose mode enabled.")
    logger.debug(f"Loaded configuration: {cfg}")

    return {"cfg": cfg, "logger": logger}
