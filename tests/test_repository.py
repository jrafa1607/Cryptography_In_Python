"""Checks that run for every notebook in Algorithms/, including new ones, with no list to maintain."""

import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted((ROOT / "Algorithms").glob("*.ipynb"))


def code(path):
    nb = json.loads(path.read_text(encoding="utf-8"))
    return "\n".join("".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "code")


def text(path):
    nb = json.loads(path.read_text(encoding="utf-8"))
    return "\n".join("".join(c["source"]) for c in nb["cells"])


def test_there_are_notebooks():
    assert NOTEBOOKS


@pytest.mark.parametrize("path", NOTEBOOKS, ids=lambda p: p.name)
def test_runs_without_user_input(path):
    """input() blocks automated execution (CI and Run all)."""
    assert "input(" not in code(path)


@pytest.mark.parametrize("path", NOTEBOOKS, ids=lambda p: p.name)
def test_keys_use_a_secure_random_generator(path):
    """The random module is predictable; key material must come from secrets or os.urandom."""
    assert not re.search(r"^\s*(import random|from random import)", code(path), re.M)


@pytest.mark.parametrize("path", NOTEBOOKS, ids=lambda p: p.name)
def test_colab_links_point_to_this_file(path):
    links = re.findall(r"blob/main/Algorithms/([^)\s\"]+\.ipynb)", text(path))
    assert all(link == path.name for link in links), f"Colab link points to {links}"
