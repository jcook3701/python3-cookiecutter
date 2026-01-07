{% import '.cookiecutter_includes/license_header.j2' as license_macros with context %}
{{- license_macros.license_header(
  cookiecutter.license,
  cookiecutter.author,
  cookiecutter.project_slug,
  file_name='__init__.py',
  comment_style='hash') -}}
