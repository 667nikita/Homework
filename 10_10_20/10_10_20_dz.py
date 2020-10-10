class Text:
    def __init__(self, name, text1, text2):
        self.name = name
        self.text1 = text1
        self.text2 = text2
        self.file = None

    def create(self):
        with open(f'{self.name}.txt', 'w') as f:
            f.write('Hello world!')

    def elem(self):
        with open(f'{self.name}.txt', 'r') as f:
            self.file = f.read()
        return len(set(self.file))

    def add_text(self):
        with open(f'{self.name}.txt', 'w') as f:
            f.write(self.text1 + self.file + self.text2)


a = Text('lol', 'kek ', ' keke')
a.create()
print(a.elem())
print(a.get_file_size())
a.add_text()
print(a.elem())
"# Homework" 
