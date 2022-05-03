chars = {
    'uppercase': '',
    'lowercase': '',
    'digit': '',
    'korean': '',
    'unknown': '',
}

for c in input():
    kind = 'unknown'
    
    if c.isupper():
        kind = 'uppercase'
    elif c.islower():
        kind = 'lowercase'
    elif c.isdigit():
        kind = 'digit'
    elif 0xAC00 <= ord(c) <= 0xD7AF:
        kind = 'korean'

    chars[kind] += c

for kind, contents in chars.items():
    print(f'{kind:9} : {contents}')
