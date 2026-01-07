{% import '.cookiecutter_includes/license_header.j2' as license_macros with context %}
{{- license_macros.license_header(
  cookiecutter.license,
  cookiecutter.author,
  cookiecutter.project_slug,
  file_name='__init__.py',
  comment_style='hash') -}}

from nutrimatic.models.metadata import Metadata

_md = Metadata.from_package("{{ cookiecutter.project_slug }}")

__version__ = _md.version
__author__ = _md.author
__license__ = _md.license
__copyright__ = _md.copyright

__all__ = [
    "__author__",
    "__copyright__",
    "__license__",
    "__version__",
]
