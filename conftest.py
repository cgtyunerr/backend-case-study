"""Pytest configurations."""

import os

import pytest


@pytest.fixture(scope="module", autouse=True)
def set_env_variable():
    os.environ["DB__NAME"] = "postgres"
    os.environ["DB__USER"] = "dbuser"
    os.environ["DB__PASS"] = "dbpass"
    os.environ["DB__HOST"] = "localhost"
    os.environ["DB__PORT"] = "5432"
