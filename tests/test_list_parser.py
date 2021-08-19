import pytest

from tld_parser.parser import parse_rule_list

from tests.fixtures import SAMPLE_INPUT


_EXPECTED = [
    ("com",),
    ("uk", "co"),
    ("ham", "wat", "lol"),
    ("香港", "政府"),
    ("გე",),
    ("ಭಾರತ",),
    ("срб", "обр"),
    ("wildcard", "*"),
    ("4i", "ub6", "6ib45", "ni64b", "456", "7245", "5432", "frhuid", "3"),
    ("it", "shit", "stupid"),
    ("it",),
]


def test_list_parser():
    assert parse_rule_list(SAMPLE_INPUT) == _EXPECTED
