# What a beautiful and entirely necessary file

class TLDParserError(Exception):
    ...


class NoRegisterablePart(TLDParserError):
    ...


class NoTLDMatch(TLDParserError):
    ...
