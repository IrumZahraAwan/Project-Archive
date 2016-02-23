def frequencyAnalysis(string, language):
    string = string.lower()
    alpha=dict([(chr(i),0) for i in range(97,123)])
    for x in string:
        if x in alpha:
          alpha[x] += 1.0
    total = len(string)
    for x in language:
        alpha[x] = alpha[x] *100 / total
    return alpha

def frequencyComparison(analysis, language):
    sum = 0
    for key in analysis:
        diff = analysis[key] - language[key]
        if analysis[key] < 0:# and analysis[key] > -1:
            analysis[key] -= 2.0
        else:
            analysis[key] += 2.0
        delta = diff**2 * (analysis[key])
        sum += abs(delta)
    return sum

def shiftAnalysis(cipher, language):
    wList = []
    for x in range(26):
        for i in range(len(cipher)):
            if cipher[i] in language:
                cipher[i] = chr((ord(cipher[i]) -96) % 26 + 97)
        decipher = (''.join(cipher))
        wList.append([(frequencyComparison(frequencyAnalysis(decipher, language), language)), decipher, 25-x])
    wList.sort(key=lambda x: x[0])
    return wList
