"""{{ cookiecutter.project_name }} Package

© All rights reserved. {{ cookiecutter.author }}

See the LICENSE file for more details.

Author: {{ cookiecutter.author }}
"""

from pathlib import Path

from pydantic import BaseModel


class CLIConfig(BaseModel):
    """
    Represents user CLI configuration for {{ cookiecutter.package_name }}.

    Attributes:
         cache_dir: (Path) {{ cookiecutter.package_name }} cache directory.
         log_file: (Path) {{ cookiecutter.package_name }} log file.
         verbose: (bool) {{ cookiecutter.package_name }} verbose mode.
    """

    cache_dir: Path = Path.home() / ".cache" / "{{ cookiecutter.package_name }}"
    log_file: Path = Path.home() / ".{{ cookiecutter.package_name }}" / "{{ cookiecutter.package_name }}.log"

    verbose: bool = False

    @property
    def log_dir(self) -> Path:
        return self.log_file.parent


DEFAULT_CONFIG = CLIConfig()
