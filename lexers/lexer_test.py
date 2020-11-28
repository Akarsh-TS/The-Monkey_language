from tokens.token import TokenType


def lexer_test():
    input = "=+-,(){};"

    tests = [
        (TokenType.ASSIGN, '='),
        (TokenType.PLUS, '+'),
        (TokenType.MINUS, '-'),
        (TokenType.COMMA, ','),
        (TokenType.LPAREN, '('),
        (TokenType.RPAREN, ')'),
        (TokenType.LBRACE, '{'),
        (TokenType.RBRACE, '}'),
        (TokenType.SEMICOLON, ';'),
    ]

    lexer = Lexer(input)
    for type, literal in tests:
        token = lexer.nextToken()
        if token.type == type and literal == token.literal:
            print("(", token.type, " : ", token.literal, ")")
        else:
            print("Test failed at: ")
            print("\tEXPECTED:")
            print("\t\t", type, " : " + literal)
            print("\tGOT")
            print("\t\t", token.type, " : " + token.literal)
