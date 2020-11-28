import enum


class TokenType(enum.Enum):
    ASSIGN = "EQUALS",
    PLUS = "+"
    MINUS = "-"
    COMMA = ','
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"
    SEMICOLON = ';'


class Token:
    def __init__(self, type: TokenType, literal: str):
        self.type = None
        self.literal = None
