import unittest

from lexers.lexer import Lexer
from tokens.token import TokenType, Token


class TokenTest(unittest.TestCase):
    def test_simple_tokens(self):
        input = "=+-,(){};"

        tests = [
            Token(TokenType.ASSIGN, "="),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.MINUS, '-'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.SEMICOLON, ';'),
        ]

        lexer_obj = Lexer(input)
        for t in tests:
            token = lexer_obj.next_token()
            self.assertEqual(token.type, t.type)
            self.assertEqual(token.literal, t.literal)


if __name__ == '__main__':
    unittest.main()
