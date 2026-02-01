{% import '.cookiecutter_includes/license/__init__.j2' as license_macros with context %}
{{- license_macros.license_header.create(
  cookiecutter.license,
  cookiecutter.copyright,
  cookiecutter.project_slug,
  file_name='test.py',
  comment_style='hash') -}}
