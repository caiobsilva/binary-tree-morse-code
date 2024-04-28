from node import Node
from search_tree import SearchTree

def build_morse_tree():
    root = Node(code='/', value=' ')
    search_tree = SearchTree(root=root)
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
    }

    for letter, code in morse_code.items():
        search_tree.insert(code, letter)

    return search_tree

def print_tree_preorder(node):
    if node:
        print(node)
        print_tree_preorder(node.left)
        print_tree_preorder(node.right)

# Construir a árvore binária do Código Morse
morse_tree = build_morse_tree()

# Imprimir a árvore usando percurso "pré-ordem"
print_tree_preorder(morse_tree.root)

# Converter um código morse para texto
morse = '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'
text = morse_tree.morse_to_text(morse)
print(f"Texto: {text}")

# Converter um texto para código morse
text = 'hello world'
morse = morse_tree.text_to_morse(text)
print(f"Código Morse: {morse}")