from __future__ import annotations

import pytest

# Try to import lance; if it fails, all tests in this directory will be skipped.
lance = pytest.importorskip("lance")


def sort_pydict(d):
    return {k: sorted(v) for k, v in d.items()}
