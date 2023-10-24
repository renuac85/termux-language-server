r"""Documents
=============
"""
import json
import os
from typing import Any, Literal

from . import FILETYPE


def get_schema(filetype: FILETYPE) -> dict[str, Any]:
    r"""Get schema.

    :param filetype:
    :type filetype: FILETYPE
    :rtype: dict[str, Any]
    """
    file = os.path.join(
        os.path.join(
            os.path.join(os.path.dirname(__file__), "assets"),
            "json",
        ),
        f"{filetype}.json",
    )
    with open(file, "r") as f:
        document = json.load(f)
    return document


def get_filetype(uri: str) -> FILETYPE | Literal[""]:
    r"""Get filetype.

    :param uri:
    :type uri: str
    :rtype: FILETYPE | Literal[""]
    """
    basename = os.path.basename(uri)
    ext = uri.split(os.path.extsep)[-1]
    if basename == "build.sh":
        return "build.sh"
    if basename.endswith(".subpackage.sh"):
        return "subpackage.sh"
    if ext == "install":
        return "install"
    if basename == "PKGBUILD":
        return "PKGBUILD"
    if ext in {"ebuild", "eclass"}:
        return "ebuild"
    if basename == "make.conf":
        return "make.conf"
    if basename == "color.map":
        return "color.map"
    return ""
