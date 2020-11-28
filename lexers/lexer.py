from tokens.token import TokenType, Token


class Lexer:
    def __init__(self, input: str):
        self.input = input
        self.position = -1
        self.read_position = 0
        self.ch = None
        self.read_char()

    def read_char(self):
        if self.read_position >= len(self.input):
            self.ch = None
        else:
            self.ch = self.input[self.read_position]
        self.position = self.read_position
        self.read_position += 1

    def next_token(self):
        ch = self.ch
        to = None
        if ch == '=':
            to = Token(TokenType.ASSIGN, ch)
        elif ch == '+':
            to = Token(TokenType.PLUS, ch)
        elif ch == '-':
            to = Token(TokenType.MINUS, ch)
        elif ch == '(':
            to = Token(TokenType.LPAREN, ch)
        elif ch == ')':
            to = Token(TokenType.RPAREN, ch)
        elif ch == '{':
            to = Token(TokenType.LBRACE, ch)
        elif ch == '}':
            to = Token(TokenType.RBRACE, ch)
        elif ch == ',':
            to = Token(TokenType.COMMA, ch)
        elif ch == ';':
            to = Token(TokenType.SEMICOLON, ch)
        else:
            to = Token(TokenType.ILLEGAL, ch)

        self.read_char()
        return to
