class Node:
    def __init__(self, code: str = '', value: str = ''):
        self.code = code
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        value = self.value
        if self.value == '':
            value = '*'
        return f"{value}: {self.code}"