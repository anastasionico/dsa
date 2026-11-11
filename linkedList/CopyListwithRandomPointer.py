# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        var = {}
        
        cur = head
        while cur:
            var[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            var[cur].next = var.get(cur.next)
            var[cur].random = var.get(cur.random)
            cur = cur.next

        cur = head
        return var[cur] if var else None
    
if __name__ == "__main__":
    first = Node(7)
    second = Node(13)
    third = Node(11)
    fourth = Node(10)
    fifth = Node(1)

    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    second.random = first
    third.random = fourth
    fourth.random = second
    fifth.random = first
    
    solution = Solution()
    result = solution.copyRandomList(first)
    while result:
        print(result.val)
        result = result.next