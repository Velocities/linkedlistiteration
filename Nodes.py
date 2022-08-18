class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

first = Node(1, Node(2, Node(3, Node(4, Node(5)))))
test = [1, 2, 3, 4, 5]