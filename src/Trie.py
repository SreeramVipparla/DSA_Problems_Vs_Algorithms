

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        
        self.children[char] = TrieNode()
        return self.children[char]

    def generate_suffix(self, suffix=''):

        suffix_of_word = []

        if suffix != ''  and self.is_word:
            suffix_of_word.append(suffix)
        
        if len(self.children) == 0:
            return suffix_of_word
        for character in self.children:
            suffix_of_word.extend(self.children[character].generate_suffix(suffix=suffix+character))

        return suffix_of_word
        
class Trie:
    def __init__(self):
        
        self.root = TrieNode()
    def insert(self, word):
        
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]
        current_node.is_word = True
    
    def find(self, prefix):
        
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        return node




MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# Test case 

# Test case 1
print(MyTrie.find("a").generate_suffix())
# Expected output
# ['nt', 'nthology', 'ntagonist', 'ntonym']

# Test case 2
print(MyTrie.find("tr").generate_suffix()) 
# Expected output
# ['ie', 'igger', 'igonometry', 'ipod']

# Edge case 1
print(MyTrie.find("").generate_suffix())  
# Expected output
# ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']

# Edge case 2 
print(MyTrie.find("b"))
# Expected output
# []
