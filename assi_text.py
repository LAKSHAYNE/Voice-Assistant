class assiText:
    def __init__(self, tk):
        self.window = tk

    def update(self, l1, stri):
        l1.configure(text=stri)
        self.window.update()
