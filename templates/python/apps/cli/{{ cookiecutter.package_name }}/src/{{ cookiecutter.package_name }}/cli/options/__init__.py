"""{{ cookiecutter.project_name }} Package

© All rights reserved. {{ cookiecutter.author }}

See the LICENSE file for more details.

Author: {{ cookiecutter.author }}
"""

from .verbose import verbose_mode
from .version import version_mode

__all__ = [
    "verbose_mode",
    "version_mode",
]
