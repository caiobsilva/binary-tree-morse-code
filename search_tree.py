from node import Node
from collections import OrderedDict

class SearchTree:
    def __init__(self, root: Node = Node()):
        self.root = root

    def search(self, code: str) -> Node:
        current = self.root
        aggregate = ''
        for symbol in code:
            aggregate += symbol
            if symbol == '.':
                if current.left is None:
                    current.left = Node(code=aggregate)
                current = current.left
            elif symbol == '-':
                if current.right is None:
                    current.right = Node(code=aggregate)
                current = current.right
        return current
    
    def parse_tree_preorder(self) -> dict:
        tree = OrderedDict()
        return self._parse_tree_preorder(self.root, tree)
    
    # Busca recursiva na árvore em pré-ordem
    def _parse_tree_preorder(self, node: Node, tree: dict) -> dict:
        if node:
            tree[node.value] = node.code
            self._parse_tree_preorder(node.left, tree)
            self._parse_tree_preorder(node.right, tree)
        return tree

    def insert(self, code: str, value: str):
        node = self.search(code)
        node.value = value
    
    def morse_to_text(self, morse_code: str) -> str:
        text = ''
        for code in morse_code.split(' '):
            node = self.search(code)
            text += node.value
        return text
    
    def text_to_morse(self, text: str) -> str:
        morse_code = ''
        characters = self.parse_tree_preorder()
        for letter in text.upper():
            morse_code += characters[letter] + ' '
        return morse_code.strip()