"""{{ cookiecutter.project_name }} Package

© All rights reserved. {{ cookiecutter.author }}

See the LICENSE file for more details.

Author: {{ cookiecutter.author }}
"""

from .config import ensure_config
from .logger import setup_logging

__all__ = [
    "ensure_config",
    "setup_logging",
]