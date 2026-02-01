{% import '.cookiecutter_includes/license/__init__.j2' as license_macros with context %}
{{- license_macros.license_header.create(
  cookiecutter.license,
  cookiecutter.copyright,
  cookiecutter.project_slug,
  file_name='__main__.py',
  comment_style='hash') -}}


from {{ cookiecutter.project_slug }}.cli.main import app


def main() -> None:
    app()


if __name__ == "__main__":
    main()
