"""{{ cookiecutter.project_name }} Package

© All rights reserved. {{ cookiecutter.author }}

See the LICENSE file for more details.

Author: {{ cookiecutter.author }}
"""

import typer

from {{ cookiecutter.package_name }}.cli.config import app as config_app
from {{ cookiecutter.package_name }}.core.config import ensure_config
from {{ cookiecutter.package_name }}.models import CLIConfig

from .options import verbose_mode, version_mode

app = typer.Typer(help="{{ cookiecutter.project_name }}: {{ cookiecutter.description }}")


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose logging."
    ),
    version: bool = typer.Option(
        None,
        "--version",
        "-V",
        callback=version_mode,
        help="Show the {{ cookiecutter.project_name }} version.",
    ),
) -> None:
    """
    Main CLI entrypoint for {{ cookiecutter.package_name }}:
    Initialize configuration and logging for all subcommands.
    """
    # Ensure config exists and load it
    cfg: CLIConfig = ensure_config()

    # Attach shared objects to context
    ctx.obj = verbose_mode(cfg, verbose)


# -----------------------------
# Register commands
# -----------------------------

# -----------------------------
# Config command:
# -----------------------------
app.add_typer(config_app, name="config")


# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    app()
