#Lab 5 Ex2 2.1
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                        self.right.insert(data)
        else:
            self.data = data
# Print the tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()
root = Node(50)       
root.insert(25)
root.insert(75)
root.insert(30)
root.insert(60)
root.insert(40)
root.insert(35)
root.insert(70)
root.insert(90)
root.insert(15)
root.insert(45)
root.insert(27)
root.insert(55)
root.insert(85)
root.insert(100)
root.PrintTree()