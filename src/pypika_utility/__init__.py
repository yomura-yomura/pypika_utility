from ._version import __version__


def fix_all():
    from . import _fixes


__all__ = [
    "fix_all"
]
