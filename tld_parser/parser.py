"""
https://www.publicsuffix.org/list/

This is NOT a public suffix parser. This is a top level domain parser.

"""

from typing import Tuple, Sequence, Union

import attr


@attr.s(slots=True, frozen=True, eq=True)
class Result:
    registrable_part: Union[Tuple[str], None] = attr.ib()
    tld: str = attr.ib()


def parse_rule_list(list_dat: Sequence[str]) -> Tuple[str]:
    """
    Take in the raw list dat file and return rules, reversed and broken
    in to labels.
    """
    rules: Tuple[str] = []

    for line in list_dat:
        # Each line is only read up to the first whitespace
        try:
            line = line.split()[0]
        except IndexError:
            continue

        # entire lines can also be commented using //
        if line.startswith("//"):
            continue

        line = line.split(".")

        if line[0].startswith("!"):
            # we don't care about cookie level shit
            continue

        line.reverse()
        rule = tuple(line)
        rules.append(rule)

    return rules


def parse_domain(tlds: Tuple[str], domain: str) -> Result:
    """
    Parse the domain and return a Result object.

    Casefold domain.
    Break domain in to labels.
    Reverse.

    For each rule of matching length, zip and compare.
    * matches all.

    """
    if not domain:
        raise ValueError("No domain given.")

    domain = domain.casefold()
    domain = domain.split(".")
    domain_labels_count = len(domain)
    domain.reverse()

    if domain_labels_count == 1:
        return None

    matches = []
    for rule in tlds:
        side_by_side = zip(domain, rule)
        for domain_label, rule_label in side_by_side:
            if domain_label != rule_label and rule_label != "*":
                break
        else:
            matches.append(rule)

    if not matches:
        return None

    # longest match wins
    matches.sort(key=len, reverse=True)
    prevailing_rule = matches[0]

    # unreverse and join for output
    tld = [label for _, label in zip(prevailing_rule, domain)]
    tld = ".".join(reversed(tld))
    registrable_part = domain[len(prevailing_rule) :]

    if not registrable_part:
        return None

    registrable_part = ".".join(reversed(registrable_part))
    return Result(tld=tld, registrable_part=registrable_part)
