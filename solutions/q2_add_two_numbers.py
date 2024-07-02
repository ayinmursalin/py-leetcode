from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def list_to_listnode(self, values: list[int]) -> Optional[ListNode]:
        if len(values) == 0:
            return None

        head = ListNode(val=values[0])
        tail = head

        i = 1
        while i < len(values):
            tail.next = ListNode(values[i])
            tail = tail.next
            
            i += 1

        return head
    
    def listnode_to_list(self, head: ListNode) -> list[int]:
        values = []
        node = head
        
        while True:
            values.append(node.val)
            node = node.next

            if node == None:
                break
        
        return values

    def add_two_numbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        str1 = ""
        str2 = ""
        node1 = l1
        node2 = l2

        while True:
            if node1 == None and node2 == None:
                total = int(str1[::-1]) + int(str2[::-1])
                list_total = [int(x) for x in str(total)]

                temp_nd = None
                for nd in list_total:
                    nd = ListNode(nd, temp_nd)
                    temp_nd = nd

                return temp_nd

            if node1 != None:
                str1 += str(node1.val)
                node1 = node1.next

            if node2 != None:
                str2 += str(node2.val)
                node2 = node2.next

