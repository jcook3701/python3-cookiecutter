"""{{ cookiecutter.project_name }} Package

© All rights reserved. {{ cookiecutter.author }}

See the LICENSE file for more details.

Author: {{ cookiecutter.author }}
"""

from .config import DEFAULT_CONFIG, CLIConfig
from .metadata import DEFAULT_METADATA, Metadata

__all__ = [
    "DEFAULT_CONFIG",
    "DEFAULT_METADATA",
    "CLIConfig",
]