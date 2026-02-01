{% import '.cookiecutter_includes/license/__init__.j2' as license_macros with context %}
{{- license_macros.license_header.create(
  cookiecutter.license,
  cookiecutter.copyright,
  cookiecutter.project_slug,
  file_name='version.py',
  comment_style='hash') -}}

import typer

import {{ cookiecutter.project_slug }} as metadata


def version_mode(version: bool) -> None:
    """
    Handle the --version / -V flag.

    When the version flag is provided, this function prints package metadata
    (version, author, license) and exits the application immediately.
    """
    if version:
        typer.echo(f"{metadata.__package__} {metadata.__version__}")
        typer.echo(f"Author: {metadata.__author__}")
        typer.echo(f"License: {metadata.__license__}")
        raise typer.Exit()
