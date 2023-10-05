# Copyright 2023 Aineko_Style Authors
# SPDX-License-Identifier: Apache-2.0
import os
import subprocess

import pytest

BASE_TEST_DATA_DIR = os.path.join(
    os.path.dirname(__file__), "test_data", "C0001"
)


def run_pylint_on_file(file_path: str) -> str:
    """Run pylint on a given file and return its output."""
    cmd = ["pylint", "--load-plugins=aineko_style.checker", file_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout


@pytest.mark.parametrize(
    "function_type,violation_type",
    [
        ("async", "with_violation"),
        ("async", "with_partial_violation"),
        ("async", "without_violation"),
        ("regular", "with_violation"),
        ("regular", "with_partial_violation"),
        ("regular", "without_violation"),
    ],
)
def test_docstring_type_checker(
    function_type: str, violation_type: str
) -> None:
    test_file_path = os.path.join(
        BASE_TEST_DATA_DIR, function_type, f"{violation_type}.py"
    )

    output = run_pylint_on_file(test_file_path)
    if violation_type == "without_violation":
        assert "docstring-contains-types" not in output
    else:
        assert "docstring-contains-types" in output
