class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):

        pass

def build_list(nodes):
    dummy = ListNode()
    current = dummy
    for val in nodes:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(" -> ".join(str(x) for x in result))


solution = Solution()

l1 = build_list([1, 2, 4])
print_list(l1)

l2 = build_list([1, 3, 4])
print_list(l2)
merged = solution.mergeTwoLists(l1, l2)

print_list(merged)
