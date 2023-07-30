class Node():
    def __init__(self, name=""):
        self.contentText = ""
        self.children = []
        self.tagName = name

    def createElement(self, name):
        return Node(name)

    def appendChild(self, child):
        self.children.append(child)

    def __str__(self, level =0):
        return 'nick __str__ todo...'



class Doc(Node):
    def __init__(self):
        self.tagName = 'html'





doc = Doc()
p1 = doc.createElement('p')
p2 = doc.createElement('p')
p1.contentText = "hello"
p2.contentText = "world"
p1.appendChild(p2)
br = doc.createElement('br')
p2.appendChild(br)

print(str(doc))