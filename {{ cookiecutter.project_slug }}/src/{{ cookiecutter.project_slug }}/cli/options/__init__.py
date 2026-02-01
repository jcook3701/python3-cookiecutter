{% import '.cookiecutter_includes/license/__init__.j2' as license_macros with context %}
{{- license_macros.license_header.create(
  cookiecutter.license,
  cookiecutter.copyright,
  cookiecutter.project_slug,
  file_name='__init__.py',
  comment_style='hash') -}}

from .verbose import verbose_mode
from .version import version_mode

__all__ = [
    "verbose_mode",
    "version_mode",
]
