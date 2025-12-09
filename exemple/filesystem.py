class VirtualFile:
    def __init__(self, name, content=""):
        self.name = name
        self.content = content

class VirtualDirectory:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def add_file(self, filename, content=""):
        self.children[filename] = VirtualFile(filename, content)

    def add_dir(self, dirname):
        self.children[dirname] = VirtualDirectory(dirname)

    def list_contents(self):
        return list(self.children.keys())

if __name__ == "__main__":
    root = VirtualDirectory("root")
    root.add_dir("docs")
    root.add_file("readme.txt", "This is PolyOS virtual fs")
    print("Root contents:", root.