"""{{ cookiecutter.project_name }} Package

© All rights reserved. {{ cookiecutter.author }}

See the LICENSE file for more details.

Author: {{ cookiecutter.author }}
Description: Entry point for running {{ cookiecutter.project_name }} via `python -m {{ cookiecutter.package_name }}`.
"""

from {{ cookiecutter.package_name }}.cli.main import app


def main() -> None:
    app()


if __name__ == "__main__":
    main()
