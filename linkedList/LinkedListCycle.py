# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise, hare = head, head

        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                return True
        return False
        

if __name__ == "__main__":
    first = ListNode(3)
    second = ListNode(2)
    third = ListNode(0)
    fourth = ListNode(-4)

    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = second

    solution = Solution()
    result = solution.hasCycle(first)
    print(result)