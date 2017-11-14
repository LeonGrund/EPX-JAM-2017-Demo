def number_needed(a, b):
    a = "".join(sorted(a))
    b = "".join(sorted(b))
    out = ""
    for c in a:
        if c in b:
            out += c
    return (len(a)+len(b)-(2*len(out)))

a = input().strip()
b = input().strip()
print(number_needed(a, b))


'''

if (len(a) == 0 or len(b) == 0):
        return 0
    a = "".join(sorted(a))
    b = "".join(sorted(b))
    ct = 0
    if a[-1:] == b[0]:
        a = a[:-1]
        b = b[1:]

    print(a)
    print(b)
    for i in a:
        for j in b:
            if i != j:
                a = a[1:]
                b = b[1:]
                ct += 1 + number_needed(a,b)
            else:
                number_needed(a[1:], b[1:])

    return ct+1

'''