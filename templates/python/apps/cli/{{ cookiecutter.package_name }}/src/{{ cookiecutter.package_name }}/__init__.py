"""{{ cookiecutter.project_name }} Package

© All rights reserved. {{ cookiecutter.author }}

See the LICENSE file for more details.

Author: {{ cookiecutter.author }}
"""

from {{ cookiecutter.package_name }}.models.metadata import Metadata

_md = Metadata.from_package("{{ cookiecutter.package_name }}")

__version__ = _md.version
__author__ = _md.author
__license__ = _md.license
__copyright__ = _md.copyright

__all__ = [
    "__author__",
    "__copyright__",
    "__license__",
    "__version__",
]
