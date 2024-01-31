class ParseError(Exception):
    pass
def parse_expression(tokens):
    term = parse_term(tokens)
    if tokens and tokens[0] == '+':
        tokens.pop(0)  
        expression = parse_expression(tokens)
        return term + expression
    return term
def parse_term(tokens):
    factor = parse_factor(tokens)
    if tokens and tokens[0] == '*':
        tokens.pop(0)  
        term = parse_term(tokens)
        return factor * term
    return factor
def parse_factor(tokens):
    if tokens and tokens[0] == '(':
        tokens.pop(0)  
        expression = parse_expression(tokens)
        if not tokens or tokens.pop(0) != ')':
            raise ParseError("Expected closing parenthesis")
        return expression
    if tokens and tokens[0].isnumeric():
        return int(tokens.pop(0))
    raise ParseError("Invalid expression")
def parse(input_string):
    tokens = list(input_string.replace(" ", ""))
    result = parse_expression(tokens)
    if tokens:
        raise ParseError("Invalid expression")
    return result
try:
    input_expression = "2 * (3 + 4)"
    result = parse(input_expression)
    print(f"Result: {result}")
except ParseError as e:
    print(f"Parse Error: {e}")
