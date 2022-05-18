"""
E ::= T | T + E | T - E
T ::= U | U * T | U / T
U ::= N | ( E ) | + U | - U
N ::= D | N
D ::= [0-9]
"""


def evaluate(s):
    return parse_expr(s)[0]


def skip_whitespace(s):
    while s and s[0].isspace():
        s = s[1:]
    return s


def parse_expr(s):
    n, s = parse_term(s)
    s = skip_whitespace(s)

    while s and s[0] in '+-':
        op, *s = skip_whitespace(s)
        k, s = parse_term(s)

        if op == '+':
            n += k
        else:
            n -= k

    return n, s


def parse_term(s):
    n, s = parse_unit(s)
    s = skip_whitespace(s)

    while s and s[0] in '*/':
        op, *s = skip_whitespace(s)
        k, s = parse_unit(s)

        if op == '*':
            n *= k
        else:
            if n % k == 0:
                n //= k
            else:
                n /= k

    return n, s


def parse_unit(s):
    s = skip_whitespace(s)

    if s and s[0] == '+':
        return parse_unit(s[1:])

    if s and s[0] == '-':
        n, s = parse_unit(s[1:])
        return -n, s

    if s and s[0] == '(':
        s = skip_whitespace(s[1:])
        n, s = parse_expr(s)
        s = skip_whitespace(s[1:])
        return n, s

    return parse_number(s)


def parse_number(s):
    n, s = 0, skip_whitespace(s)

    while s and s[0].isdigit():
        d, *s = s
        n = 10 * n + int(d)

    s = skip_whitespace(s)
    return n, s


def main():
    print(evaluate(input()))


if __name__ == '__main__':
    main()
