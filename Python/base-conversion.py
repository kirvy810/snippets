def from_digit(n):
    """
    0 <= n < 16
    """
    return '0123456789ABCDEF'[n]


def to_base(n, b):
    if n < 0:
        return '-' + to_base(-n, b)
    
    q, r = divmod(n, b)
    
    if q == 0:
        return from_digit(r)
    return to_base(q, b) + from_digit(r)


def base2(n):
    return to_base(n, 2)


def base8(n):
    return to_base(n, 8)


def base16(n):
    return to_base(n, 16)


n = int(input()) 
print(base2(n))
print(base8(n))
print(base16(n))
