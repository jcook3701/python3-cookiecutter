"""{{ cookiecutter.project_name }} Package

© All rights reserved. {{ cookiecutter.author }}

See the LICENSE.TXT file for more details.

Author: {{ cookiecutter.author }}
Description: Entry point for running {{ cookiecutter.project_name }} via `python -m {{ cookiecutter.package_name }}`.
"""

from .{{ cookiecutter.package_name }} import main

if __name__ == "__main__":
    main()
