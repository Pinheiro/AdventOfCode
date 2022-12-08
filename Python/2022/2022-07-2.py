class TreeNode(object):

    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.size = 0
        self.parent = parent
    
    def AddChild(self, name):
        node = TreeNode(name, self)
        self.children.append(node)

    def GetChild(self, name):
        "returns a child node by name"
        for child in range(0, len(self.children)):
            if(self.children[child].name == name):
                return self.children[child]
    
    def GetRoot(self):
        node = self
        while node.parent != None:
            node = node.parent
        return node
    
    def Resize(self, node):
        for child in node.children:
            self.Resize(child)
            node.size += child.size
    
#fileName = "_Input/2022-07-1.inputTestA"
fileName = "_Input/2022-07-1.inputPuzzle"
input = [x.strip() for x in open(fileName, "r").readlines()]

tree = None
folderName = ""
for line in input:
    if line[0:5] == "$ cd ":
        folderName = line[5:]
        if tree == None:
            tree = TreeNode(folderName, None)
        elif folderName == "..":
            tree = tree.parent
        else:
            tree = tree.GetChild(folderName)
    elif line[0:4] == "$ ls": 
        pass
    elif line[0:4] == "dir ": 
        folderName = line[4:]
        tree.AddChild(folderName)
    else:
        size = int(line.split(" ")[0])
        tree.size += size

tree = tree.GetRoot()
tree.Resize(tree)
freeSpace = 70000000-tree.size
stillRequired = 30000000-freeSpace
smallestSize = tree.size

def GetSmallestSize(node):
    global smallestSize
    if (node.size-stillRequired >= 0) and (node.size < smallestSize): smallestSize = node.size
    for child in node.children: GetSmallestSize(child)

GetSmallestSize(tree)
print(smallestSize)