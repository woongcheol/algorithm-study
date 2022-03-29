class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self, head):
        self.head = head
    
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
    
    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False        

    def delete(self, value):
        searched = False
        self.parent = self.head
        self.change_node_parent = self.head 
        self.current_node = self.head

        while self.current_node:

            # 탐색
            if self.current_node.value == value:
                searched = True
                break

            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left


            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if searched == False:
            return False

        # 노드 삭제
        if searched:

            # leaf node 삭제
            if self.current_node.left == None and self.current_node.right == None:
                if value < self.parent.value:
                    self.parent.left = None
                else:
                    self.parent.right = None
                del self.current_node

            # child node 2개인 node 삭제
            elif self.current_node.left != None and self.current_node.right != None:
                self.delete_node = self.current_node
                self.current_node = self.current_node.right
                

                while self.current_node.left != None:
                    self.change_node_parent = self.current_node
                    self.current_node = self.current_node.left


                if self.parent.left.value == value:
                    
                    # 추가 - 바꿀 노드의 Child Node가 있을 경우
                    if self.current_node.right != None:
                        self.change_node_parent.left = self.current_node.right
                        self.parent.left = self.current_node
                        self.current_node.left = self.delete_node.left
                        self.current_node.right = self.delete_node.right
                        
                    else:
                        self.change_node_parent.left = None
                        self.parent.left = self.current_node
                        self.current_node.left = self.delete_node.left
                        self.current_node.right = self.delete_node.right
                else:
                    
                    # 추가 - 바꿀 노드의 Child Node가 있을 경우
                    if self.current_node.right:
                        self.change_node_parent.left = self.current_node.right
                        self.parent.right = self.current_node
                        self.current_node.left = self.delete_node.left
                        self.current_node.right = self.delete_node.right
                        
                    else:
                        self.change_node_parent.left = None
                        self.parent.right = self.current_node
                        self.current_node.left = self.delete_node.left
                        self.current_node.right = self.delete_node.right

            # child node 1개인 node 삭제
            elif self.current_node.left != None or self.current_node.right != None:
                if self.current_node.left != None:
                    if self.parent.left.value == value:
                        self.parent.left = self.current_node.left
                    else:
                        self.parent.right = self.current_node.left

                else:
                    if self.parent.left.value == value:
                        self.parent.left = self.current_node.right
                    else:
                        self.parent.right = self.current_node.right
            
        return '삭제가 완료되었습니다'

# Leaf Node 삭제
'''
BST = NodeMgmt(Node(10))
BST.insert(5)
BST.insert(15)
BST.insert(3)
BST.insert(6)
BST.insert(19)

print(BST.search(19)) # True 
print(BST.search(3)) # True 

print(BST.delete(19)) # None
print(BST.search(19)) # False

print(BST.delete(3)) # None
print(BST.search(3)) # False

print(BST.search(5)) # True
'''

# Child Node가 2개인 경우 삭제
BST = NodeMgmt(Node(10))
BST.insert(7)
BST.insert(15)
BST.insert(6)
BST.insert(8)
BST.insert(13)
BST.insert(18)
BST.insert(11)
BST.insert(12)
BST.insert(16)
BST.insert(19)
BST.insert(17)

print(BST.search(15)) # 삭제될 노드 - True 
print(BST.search(16)) # 교체될 노드 - True 
print(BST.search(17)) # 교체될 노드 자식 노드 - True 

print(BST.delete(15)) # None
print(BST.search(15)) # False

print(BST.search(17)) # True
print(BST.search(13)) # 교체된 노드의 자식 노드 - True
print(BST.search(18)) # 교체된 노드의 자식 노드 - True