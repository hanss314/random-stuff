def S(x):
    def Sx(y):
        def Sxy(z):
            return (x, z), (y, z)
        return Sxy
    return Sx

def K(x):
    def Kx(y):
        return x
    return Kx

def I(x):
    return x

def find_matching_paren(s, p):
    count = 1
    start = s[p]
    if start == '(':
        matching = ')'
        direction = 1
    elif start == ')':
        matching = '('
        direction = -1
    else:
        return -1

    while 0 <= p < len(s):
        p += direction
        if s[p] == start: count += 1
        elif s[p] == matching: count -= 1

        if count == 0: return p

    return -1
    

def parse(s):
    s = s.replace(' ', '').replace('\n', '').replace('\t', '') 
    while len(s) != 0 and s[0] == '(' and find_matching_paren(s, 0) == len(s)-1:
        s = s[1:-1]
    if len(s) == 0: return ()

    if s[0] == '(': 
        other = find_matching_paren(s, 0)
        return parse(s[1:other]), parse(s[other+1:])
    elif len(s) == 1: return s
    else:
        if s[-1] == ')': split = find_matching_paren(s, len(s)-1)
        else: split = -1
        return parse(s[:split]), parse(s[split:])

def toSKI(c):
    if c == 'S': return S
    elif c == 'K': return K
    elif c == 'I': return I
    else: return c

def tostr(c):
    if c == S: return 'S'
    elif c == K: return 'K'
    elif c == I: return 'I'
    else: return c

def teval(tree):
    left, right = tree
    if isinstance(toSKI(left), str): return left, right
    if isinstance(left, tuple): left = teval(left)
    if isinstance(right, tuple): right = teval(right)
    left = toSKI(left)
    right = toSKI(right)
    if isinstance(left, str) or isinstance(left, tuple): return left, right
    f = left(right)
    if isinstance(f, tuple): return teval(f)
    else: return f

def run(s):
    return teval(parse(s))
