from datetime import date

import pytest

from demo_app.date_utils import parse_iso_date


def test_parse_iso_date_returns_date():
    assert parse_iso_date("2026-08-26") == date(2026, 8, 26)


def test_parse_iso_date_rejects_invalid_value():
    with pytest.raises(ValueError):
        parse_iso_date("not-a-date")
