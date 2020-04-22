def longestStringChain(strings):
    stringChains = {}
    for string in strings:
        stringChains[string] = {"nextString": "", "maxChainLen": 1}

    sortedString = sorted(strings, key=len)
    for string in sortedString:
        findLongestStringChain(string, stringChains)

    return buildLongestStringChain(strings, stringChains)


def findLongestStringChain(currentString, stringChains):
    for i in range(len(currentString)):
        smallerString = currentString[:i] + currentString[i + 1:]
        if smallerString in stringChains:
            smallerStringChainLen = stringChains[smallerString]["maxChainLen"]
            currentStringChainLen = stringChains[currentString]["maxChainLen"]
            if smallerStringChainLen + 1 > currentStringChainLen:
                stringChains[currentString]["maxChainLen"] = smallerStringChainLen + 1
                stringChains[currentString]["nextString"] = smallerString


def buildLongestStringChain(strings, stringChains):
    maxChainLen = 0
    chainStartingString = ""
    for string in strings:
        if stringChains[string]["maxChainLen"] > maxChainLen:
            maxChainLen = stringChains[string]["maxChainLen"]
            chainStartingString = string

    longestStringChain = []
    currentString = chainStartingString
    while currentString != "":
        longestStringChain.append(currentString)
        currentString = stringChains[currentString]["nextString"]
    return [] if len(longestStringChain) == 1 else longestStringChain






