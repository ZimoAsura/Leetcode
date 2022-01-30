# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 链表题技巧：设置虚拟头节点，避免需要处理空指针的情况
        # 如果不设置虚拟头节点，删除头节点的操作与删除其他节点的操作不一样
        # 感觉所有设置到需要删除链表节点的题目都可以通过设置虚拟头节点来简化代码
        dummy = ListNode(None)
        p = dummy
        p.next = head
        p1 = head
        # 单链表无法向前遍历
        # 所以还需要一个节点用来记录当前节点的上一个节点
        while p1 != None:
            if p1.val == val:
                p1 = p1.next
                p.next = p1
            else:
                p1 = p1.next
                p = p.next
        return dummy.next