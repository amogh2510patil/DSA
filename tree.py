class TreeNode:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []
    
    def addChild(self,child):
        child.parent = self
        self.children.append(child)
    
    def getLevel(self):
        par = self.parent
        lev = 0
        while par:
            lev +=1
            par = par.parent
        return lev
    def printTree(self):
        pretty = "-" * self.getLevel() *3
        print(pretty,self.data)
        for child in self.children:
            child.printTree() 
            
root = TreeNode("Tech")

laptop = TreeNode("Laptop")
root.addChild(laptop)
laptop.addChild(TreeNode("Lenovo"))
laptop.addChild(TreeNode("Asus"))
laptop.addChild(TreeNode("Dell"))

mobile = TreeNode("Mobiles")
root.addChild(mobile)
mobile.addChild(TreeNode("One Plus"))
mobile.addChild(TreeNode("Iphone"))
mobile.addChild(TreeNode("Samsung"))

root.printTree()