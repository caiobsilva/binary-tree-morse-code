from node import Node
from search_tree import SearchTree
import os

def build_morse_tree():
    root = Node(code='/', value=' ')
    search_tree = SearchTree(root=root)
    
    morse_dict = {}
    with open('morse', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                key, value = line.split(' ')
                morse_dict[key] = value

    for letter, code in morse_dict.items():
        search_tree.insert(code, letter)

    return search_tree

def print_tree_preorder(node):
    if node:
        print(node)
        print_tree_preorder(node.left)
        print_tree_preorder(node.right)

def translate_text_to_morse(text):
    morse = morse_tree.text_to_morse(text)
    return morse

def translate_morse_to_text(morse):
    text = morse_tree.morse_to_text(morse)
    return text

def translate_file_to_morse(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    morse = morse_tree.text_to_morse(text)
    return morse

def translate_file_to_text(filepath):
    with open(filepath, 'r') as file:
        morse = file.read()
    text = morse_tree.morse_to_text(morse)
    return text

# Construir a árvore binária do Código Morse
morse_tree = build_morse_tree()

while True:
    print("\n\n")
    print("Tradutor código Morse")
    print("1. Traduzir texto para código Morse")
    print("2. Traduzir código Morse para texto")
    print("3. Traduzir código Morse de um arquivo para texto")
    print("4. Traduzir texto de um arquivo para código Morse")
    print("5. Imprimir a árvore de busca em pré-ordem")
    print("6. Exit")

    option = input("Selecione uma opção: ")

    os.system('clear')
    print("\n\n")

    if option == "1":
        text = input("Insira o texto desejado: ")
        morse = translate_text_to_morse(text)
        print(f"Código Morse: {morse}")
    elif option == "2":
        morse = input("Insira o código morse desejado: ")
        text = translate_morse_to_text(morse)
        print(f"Texto: {text}")
    elif option == "3":
        filepath = input("Insira o nome do arquivo do código Morse: ")
        text = translate_file_to_text(filepath)
        print(f"Código Morse: {text}")
    elif option == "4":
        filepath = input("Insira o nome do arquivo contendo o texto: ")
        text = translate_file_to_morse(filepath)
        print(f"Texto: {text}")
    elif option == "5":
        print_tree_preorder(morse_tree.root)
    elif option == "6":
        break
    else:
        print("Opção inválida. Tente novamente.")
