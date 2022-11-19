#Lab5 Ex2 2.2
class Node:
  
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
  
def insert(node, data):
  
    if node is None:
        return Node(data)

    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
  
    return node
  
def deleteNode(root, data):
  
    if root is None:
        return root
  
    if data < root.data:
        root.left = deleteNode(root.left, data)
        return root
  
    elif(data > root.data):
        root.right = deleteNode(root.right, data)
        return root
  
    if root.left is None and root.right is None:
          return None
  
    if root.left is None:
        temp = root.right
        root = None
        return temp
  
    elif root.right is None:
        temp = root.left
        root = None
        return temp
  
    succParent = root
    
    succ = root.right
  
    while succ.left != None:
        succParent = succ
        succ = succ.left

    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right
  
    root.data = succ.data
  
    return root
  
  
root = None
root = insert(root, 50)
root = insert(root, 25)
root = insert(root, 75)
root = insert(root, 30)
root = insert(root, 60)
root = insert(root, 40)
root = insert(root, 35)
root = insert(root, 70)
root = insert(root, 90)
root = insert(root, 15)
root = insert(root, 45)
root = insert(root, 27)
root = insert(root, 55)
root = insert(root, 85)
root = insert(root, 100)

  
print("\nDelete 30,75,35")
print("\n")
root = deleteNode(root, 30)
root = deleteNode(root, 75)
root = deleteNode(root, 35)
print("Inorder traversal of the modified tree")
inorder(root)