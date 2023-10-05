# Copyright 2023 Aineko_Style Authors
# SPDX-License-Identifier: Apache-2.0
"""Module to define a custom pylint checker to detect types in docstrings."""
import re

from astroid.nodes import FunctionDef
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker
from pylint.lint import PyLinter


class DocstringTypeChecker(BaseChecker):
    """Checker to detect types in docstrings."""

    __implements__ = IAstroidChecker

    name = "docstring-type-checker"
    msgs = {
        "C0001": (
            "Docstring contains types. Types should be part of the function"
            " definition.",  # template of displayed message
            "docstring-contains-types",  # message symbol
            "Types should be part of the function definition and not the"
            " docstring.",  # Message description
        ),
    }

    priority = -1

    # Regex pattern to detect types in docstrings
    # This pattern will match: parameter_X (type): description
    _TYPE_PATTERN = re.compile(r"\w+ \(\w+\):")

    def _check_docstring_for_types(self, node: FunctionDef) -> None:
        """Utility method to check docstrings for types."""
        if node.doc:
            if ":type" in node.doc or self._TYPE_PATTERN.search(node.doc):
                self.add_message("docstring-contains-types", node=node)

    def visit_functiondef(self, node: FunctionDef) -> None:
        """Called for every function or method definition in the source code."""
        self._check_docstring_for_types(node)

    def visit_asyncfunctiondef(self, node: FunctionDef) -> None:
        """Called for every asynchronous function or method definition in the source code."""
        self._check_docstring_for_types(node)


def register(linter: PyLinter) -> None:
    """Required method to auto-register this checker."""
    linter.register_checker(DocstringTypeChecker(linter))
