# -*- coding: utf-8 -*-
"""Tests for `topalias` package."""

import pytest

from click.testing import CliRunner
from bs4 import BeautifulSoup
import requests

from topalias import topalias
from topalias import cli


@pytest.fixture(name="response")
def fixture_response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    return requests.get('https://github.com/CSRedRat/topalias')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""

    assert 'GitHub' in BeautifulSoup(response.content).title.string


@pytest.mark.parametrize(('message', 'expected'), [
    ('test', 'topalias util test\n'),
])
def test_welcome(capsys, message, expected):
    """Test output to stdout"""
    topalias.welcome(message)
    out, err = capsys.readouterr()
    assert out == expected, err == ''


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result_output = runner.invoke(cli.main)
    assert result_output.exit_code == 0
    assert 'https://github.com/CSRedRat/topalias' in result_output.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
