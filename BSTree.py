class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def addChild(self,data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BSTNode(data)
        
        else : 
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BSTNode(data)
    
    def inorder(self):
        elements = []
        
        if self.left:
            elements += self.left.inorder()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.inorder()
        return elements
    
    def search(self,data):
        if data == self.data:
            return True
        
        elif data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        
        else :
            if self.right:
                return self.right.search(data)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else :
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calcSum(self):
        sum = self.data
        if self.left:
            sum += self.left.calcSum()
        if self.right:
            sum += self.right.calcSum()
        return sum
    
    def preTraversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.preTraversal()
        if self.right:
            elements += self.right.preTraversal()
        return elements

    def delNode(self,data):
        if data < self.data:
            if self.left:
                self.left = self.left.delNode(data)
        
        elif data > self.data:
            if self.right:
                self.right = self.right.delNode(data)
        
        else:
            if not self.left and not self.right:
                return None
            if not self.left :
                return self.right
            min = self.right.find_min()
            self.data = min
            self.right = self.right.delNode(min)
        
        return self






lst = [17,2,23,54,27,90,10,1,3,5]
root = BSTNode(lst[0])
for i in range(1,len(lst)):
    root.addChild(lst[i])

print(root.inorder())
print(root.search(90))
print(root.find_min())
print(root.find_max())
print(root.calcSum())
print(root.preTraversal())
root = root.delNode(17)
print(root.preTraversal())