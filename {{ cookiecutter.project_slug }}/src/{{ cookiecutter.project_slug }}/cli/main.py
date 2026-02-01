{% import '.cookiecutter_includes/license/__init__.j2' as license_macros with context %}
{{- license_macros.license_header.create(
  cookiecutter.license,
  cookiecutter.copyright,
  cookiecutter.project_slug,
  file_name='main.py',
  comment_style='hash') -}}

import typer

from .options import verbose_mode, version_mode


app = typer.Typer(help="{{ cookiecutter.project_slug }}: {{ cookiecutter.description }}")


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
        help="Show the {{ cookiecutter.project_slug }} version.",
    ),
) -> None:
    """
    Main CLI entrypoint for {{ cookiecutter.project_slug }} Cookiecutter utilities:
    Initialize configuration and logging for all subcommands.
    """
    # Ensure config exists and load it
    cfg: CLIConfig = ensure_config()

    # Attach shared objects to context
    ctx.obj = verbose_mode(cfg, verbose)


# -----------------------------
# Register commands
# -----------------------------
# {{ cookiecutter.project_slug }} commands:
# -----------------------------


# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    app()
