[![Build Status](https://travis-ci.org/theelous3/sansio-tld-parser.svg?branch=master)](https://travis-ci.org/github/theelous3/sansio-tld-parser/branches)


### A sansio tld parser.

Given a tld rule list and a domain, parse the tld from the domain.

Yes, it's more complicated than `domain.split(".")` ;)


### Why is this sansio? What has io got to do with it?

Parsing TLDs requires actually knowing all of the TLDS. These are maintained in a list online.

For some reason, all of the TLD parsers out that at the moment like to handle lookups to these lists internally, making them awkward to couple with whatever your flavour of application is.

This is a get-the-list-yourself situation.

### Installation

`pip install tld-parser` :)

### Use

You'll need access to the public suffix list:

Canonical: https://publicsuffix.org/list/public_suffix_list.dat

Git hosted: https://raw.githubusercontent.com/publicsuffix/list/master/public_suffix_list.dat

```python
>>> from tld_parser import parse_rule_list, parse_domain
>>>
>>> from some_http_client import get
>>>
>>> suffix_list = get(list_url).content
>>> # The parser expects a Sequence of rules in the same format at the public suffix list.
>>> suffix_list = suffix_list.decode().splitlines()
>>>
>>> tld_rules = parse_rule_list(suffix_list)
>>>
>>> parse_domain(tld_rules, "some_subdomain.domain.co.uk")
Result(registrable_part='some_subdomain.domain', tld='co.uk')
```

And out pops a `Result` object :)
