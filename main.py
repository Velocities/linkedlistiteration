#You are given a Linked List with integer Nodes
#You must reverse the Linked List and run your code to see if it runs
from Nodes import *
from time import perf_counter

def getVals(obj, a_list) -> None:
    a_list.append(obj.val)
    if obj.next == None:
        return
    else:
        getVals(obj.next, a_list)

class Solution:
    def __init__(self, myNode=None):
        self.myNode = myNode

    def main(self, head) -> Node:
        myVals = []
        try:
            getVals(head, myVals)
        except AttributeError:
            return head
        myVals.reverse()
        counter = 0
        for i in myVals:
            if counter == 0:
                start = Node(i)
            elif counter == 1:
                tmp = Node(i)
                start.next = tmp
            else:
                tmp.next = Node(i)
                tmp = tmp.next
            counter += 1
        return start

if __name__ == '__main__':
    Final = Solution(first)
    test_me = [i for i in test[::-1]]
    s = perf_counter()
    Answer = Final.main(Final.myNode)
    elapsed = perf_counter() - s
    check = []
    getVals(Answer, check)
    with open("results.txt", "a") as f:
        if check == test_me:
            f.write(f"Main.py succeeded in {elapsed} seconds\n")
        else:
            f.write(f"Main.py failed in {elapsed} seconds\n")