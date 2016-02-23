import frequencylib

english = {'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09, 'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23, 'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15, 'q': 0.10, 'z': 0.07}

def decipher(cipher, language=english, minKeyLen=4, keyLenList=[]):
    cipherLower = ''.join(c for c in cipher.lower() if c in english)
    if keyLenList == []:
        
        # Find repeating patterns
        setsof3 = {}
        for i in range(len(cipherLower)-2):
            tri = cipherLower[i:i+3]
            setsof3[tri] = setsof3.get(tri, []) + [i+1]
        listi = [setsof3[key] for key in setsof3 if len(setsof3[key])>2]
        
        # Find the most common differences
        diff = []
        for i in listi:
            diff += [abs(i[y] - i[y+x]) for y in range(len(i)-1) for x in range(1, len(i)-y)]
        factorl = {}
        for x in diff:
            factors = [n for n in range(minKeyLen,int(x**0.5)) if x%n == 0]
            for f in factors:
                    factorl[f+0.0] = factorl.get(f+0.0, 1) + 1
        factorl = sorted(factorl, key=factorl.get, reverse=True)
        if not factorl:
            return []
        for x in factorl[:4]:
            keyLenList.append(int(x))
    returnlist = []
    for keyLen in keyLenList:
        splitList = []
        for single in range(keyLen):
            splitList.append([cipherLower[iter] for iter in range(single, len(cipherLower), keyLen) ])

        # Determine key using frequency analysis
        key = ''.join([chr(frequencylib.shiftAnalysis(split, language)[0][2]+97) for split in splitList])

        # Return the clear text
        i = 0
        cipherlist = list(cipher.lower())
        for l in range(len(cipherlist)):
            if cipherlist[l] in language:
                letter = ord(key[i])-97
                cipherlist[l] = chr((ord(cipherlist[l])-97-letter)%26 + 97)
                i=(i+1)%keyLen
        cipherlist = ''.join(cipherlist)
        returnlist.append([frequencylib.frequencyComparison(frequencylib.frequencyAnalysis(cipherlist, language), language), cipherlist, key])#+' ('+secondary+')'])
    return returnlist
