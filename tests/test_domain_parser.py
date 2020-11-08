import pytest

from tld_parser.parser import Result, parse_domain, parse_rule_list

from tests.fixtures import SAMPLE_INPUT


TLDS = parse_rule_list(SAMPLE_INPUT)


@pytest.mark.parametrize(
    "domain, expected",
    [
        ["com", None],
        ["co.uk", None],
        ["bread.com", Result(registrable_part="bread", tld="com")],
        ["blah.bread.com", Result(registrable_part="blah.bread", tld="com")],
        ["bread.co.uk", Result(registrable_part="bread", tld="co.uk")],
        ["税.政府.香港", Result(registrable_part="税", tld="政府.香港")],
        ["lol.wat.wildcard", Result(registrable_part="lol", tld="wat.wildcard")],
        [
            "huehuehue.3.frhuid.5432.7245.456.ni64b.6ib45.ub6.4i",
            Result(
                registrable_part="huehuehue",
                tld="3.frhuid.5432.7245.456.ni64b.6ib45.ub6.4i",
            ),
        ],
    ],
)
def test_parse_domain(domain, expected):
    assert parse_domain(TLDS, domain) == expected
