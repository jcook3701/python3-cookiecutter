"""{{ cookiecutter.project_name }} Package

© All rights reserved. {{ cookiecutter.author }}

See the LICENSE file for more details.

Author: {{ cookiecutter.author }}
"""

import typer

import {{ cookiecutter.package_name }} as pkg


def version_mode(version: bool) -> None:
    """
    Handle the --version / -V flag.

    When the version flag is provided, this function prints package metadata
    (version, author, license) and exits the application immediately.
    """
    if version:
        typer.echo(f"{pkg.__name__} {pkg.__version__}")
        typer.echo(f"Author: {pkg.__author__}")
        typer.echo(f"License: {pkg.__license__}")
        raise typer.Exit()
