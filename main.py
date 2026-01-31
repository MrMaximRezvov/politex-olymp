

alph = {
    'a': 'q1z',
    'h': 'i8k',
    'o': 'g5h',
    'v': 'c2v',
    'b': 'w2x',
    'i': 'o9l',
    'p': 'h6j',
    'w': 'v3b',
    'c': 'e3c',
    'j': 'p0p',
    'q': 'j7k',
    'x': 'b4n',
    'd': 'r4v',
    'k': 'a1s',
    'r': 'k8l',
    'y': 'n5m',
    'e': 't5b',
    'l': 's2d',
    's': 'l9z',
    'z': 'm6q',
    'f': 'y6n',
    'm': 'd3f',
    't': 'z0x',
    ' ': 'sp0',
    'g': 'u7m',
    'n': 'f4g',
    'u': 'x1c'
}

reverse_alph = {v: k for k, v in alph.items()}

def main():
    n = input()

    s = ''
    sarr = []
    for i in range(0, len(n), 3):
        s = n[i] + n[i+1] + n[i+2]
        # print(s)
        sarr.append(s)
    print('decrypt inp s')
    ans = decrypt(sarr, reverse_alph)
    print(ans)
    
    print('encrypr inp your s')
    su = input()
    ans = encrypt(su, alph)
    print(ans)





    

def decrypt(sarr, alph):
    ans = ''
    for i in range(len(sarr)):
        ans += alph.get(sarr[i])
        print(i, '=', ans)
    return ans

def encrypt(s, alph):
    ans = ''
    for i in range(len(s)):
        ans += alph.get(s[i])
        print(i, '=', ans)
    return ans


if __name__ == '__main__':
    main()