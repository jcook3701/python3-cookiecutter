"""{{ cookiecutter.project_name }} Package

© All rights reserved. {{ cookiecutter.author }}

See the LICENSE file for more details.

Author: {{ cookiecutter.author }}
"""

from collections.abc import Mapping
from importlib.metadata import PackageNotFoundError, metadata
from typing import cast

from pydantic import BaseModel


class Metadata(BaseModel):
    """
    metadata type.

    Attributes:
        version: (str).
        author: (str).
        license: (str).
        copyright: (str).
    """

    version: str = ""
    author: str = ""
    license: str = ""

    @property
    def copyright(self) -> str:
        return f"2025 {self.author}"

    @classmethod
    def from_package(cls, package_name: str = "{{ cookiecutter.package_name }}") -> "Metadata":
        """
        Create Metadata from the installed package metadata.

        Falls back to defaults if the package is not found.
        """
        try:
            pkg_meta = metadata(package_name)
            pkg_meta_dict = cast(Mapping[str, str], pkg_meta)

            return cls(
                version=pkg_meta_dict.get("Version", "{{ cookiecutter.version }}"),
                author=pkg_meta_dict.get("Author", "{{ cookiecutter.author }}"),
                license=pkg_meta_dict.get("License", "MIT"),
            )
        except PackageNotFoundError:
            return DEFAULT_METADATA


DEFAULT_METADATA = Metadata(version="{{ cookiecutter.version }}", author="{{ cookiecutter.author }}", license="MIT")
