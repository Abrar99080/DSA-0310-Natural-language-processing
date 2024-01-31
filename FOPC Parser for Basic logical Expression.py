from pyparsing import Word, alphas, infixNotation, opAssoc, Group, Suppress
variable = Word(alphas, exact=1)
constant = Word(alphas.upper(), exact=1)
and_op = Suppress('&')
or_op = Suppress('|')
not_op = Suppress('~')
expr = infixNotation(
    variable | constant,
    [
        (not_op, 1, opAssoc.RIGHT),
        (and_op, 2, opAssoc.LEFT),
        (or_op, 2, opAssoc.LEFT),
    ],
)
def parse_fopc(input_string):
    return expr.parseString(input_string, parseAll=True)[0]
if __name__ == "__main__":
    input_string = "P & (Q | ~R)"
    parsed_expr = parse_fopc(input_string)
    print(f"Input: {input_string}")
    print(f"Parsed: {parsed_expr}")
