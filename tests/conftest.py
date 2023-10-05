# Copyright 2023 Aineko_Style Authors
# SPDX-License-Identifier: Apache-2.0
"""Pytest configuration file.

Fixtures are defined in the `tests/fixtures` directory and are automatically
discovered and loaded by pytest. They can be grouped in (sub)directories or be
defined in a single file, as long as they are stored within `tests/fixtures`.
"""
from glob import glob

pytest_plugins = [
    fixture_file.replace("/", ".").replace(".py", "")
    for fixture_file in glob("tests/fixtures/**/[!__]*.py", recursive=True)
]
