from datetime import date

from dateutil.parser import isoparse


def parse_iso_date(value: str) -> date:
    return isoparse(value).date()
