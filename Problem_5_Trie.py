#!/usr/bin/env python
# coding: utf-8


# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
    def insert(self, char):
        self.children[char] = TrieNode()
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        
        current_node = self.root

        for character in word:
            if character not in current_node.children:
                current_node.insert(character)
            current_node = current_node.children[character]

        current_node.is_word = True

    def find(self, prefix):
        
        current_node = self.root
        for letter in prefix:
            current_node = current_node.children[letter]
        
        return current_node


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix=''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        
        path_dict = self.children
        
        output_list = []
        
        for key, value in path_dict.items():
            suffix += key
            if value.is_word:
                output_list.append(suffix)
            else:
                output_list += value.suffixes(suffix)
        return output_list


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)




from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');



