entries = ["carl", "frank", "francis", "ferdinard", "chris", "eric", "ernest", "adam", "andrew", "alex"]
# entries = ["ca", "fr", "fa", "ch", "m"]

class TrieNode():
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}


class Trie():
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new = TrieNode(char)
                node.children[char] = new
                node = new
        node.is_end = True

    def _dfs(self, node, prefix):
        if node.is_end:
            self.output.append(prefix + node.char)
        else:
            for child in node.children.values():
                self._dfs(child, prefix + node.char)

    def query(self, word):
        self.output = []
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        self._dfs(node, word[:-1])

        return sorted(self.output)


    def traverse(self, node="start", level=1):
        if node == "start":
            node = self.root
        for i in node.children:
            print(f"Level {level} : {i}")
            child = node.children[i]
            self.traverse(node=child, level=level+1)
            if not child.children:
                print("---")



my_trie = Trie()
for i in entries:
    my_trie.insert(i)
# print(my_trie.query("fr"))

my_trie.traverse()
