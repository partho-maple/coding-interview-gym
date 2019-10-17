# https://www.algoexpert.io/questions/Suffix%20Trie%20Construction

"""
 The way we can build our Suffix-Trie is to use a bunch of hash tables or dictionaries. Where every node in the suffix
 tree is gonna be a Key in a dictionary, pointing to another dictionary/HashTable (the value of the key will store of
 the next node's dictionary directly so basically, it will be a nested dictionary of dictionary). And all the values in
 the dictionary, will be the other nodes in the tree whose keys will be a specific letter that comes after the previous
 letter, and that points to another hash table, and so on and so forth.

Sample input (for creation):"babc"
Sample output (for creation):
{
"c": {"*": True},
"b": {
        {"c": {"*": True},
        {"a": {"b":
                    {"c": {"*": True}}},
     },
"a": {
        "b":
             {"c": {"*": True}}},
}
"""


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





st = SuffixTrie("babc")
contains = st.contains("bc")
print("Restlt: ", contains)


