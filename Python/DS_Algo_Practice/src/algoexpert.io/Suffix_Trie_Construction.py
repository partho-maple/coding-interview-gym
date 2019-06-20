# https://www.algoexpert.io/questions/Suffix%20Trie%20Construction


class SuffixTrie:

    def __init__(self, string):
        self.root ={}
        self.end_symbol = "*"
        self.populate_suffix_trie_from(string)

    def populate_suffix_trie_from(self, string):
        for i in range(len(string)):
            self.insert_substring_starting_at(i, string)

    def insert_substring_starting_at(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.end_symbol] = True

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in string:
                return False
            node = node[letter]
        return self.end_symbol in node


