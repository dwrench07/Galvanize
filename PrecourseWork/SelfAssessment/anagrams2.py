def anagrams(word_list):
    d = {}
    out = set()
    for word in word_list:
        s = ''.join(sorted(word))
        print(word)
        try:
            out.add(d[s])
            out.add(word)
            print(s)
        except:
            d[s] = word
            print(word)
    return out

anagrams(['is', 'si', 'top', 'spot', 'pot', 'clack', 'clack'])
