from collections import defaultdict
def groupAnagrams(words):
    anagrams = defaultdict(list)
	for word in words:
		sortedWord = "".join(sorted(word))
		anagrams[sortedWord].append(word)
	return list(anagrams.values())