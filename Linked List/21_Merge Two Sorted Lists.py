# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = nextclass Solution:
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 链表题技巧：设置虚拟头节点dummy,有了dummy节点可以避免处理空指针的情况
        dummy = ListNode(None)
        p = dummy
        p1 = list1
        p2 = list2
        while p1 != None and p2 != None:
            # 判断结点值大小，较小的节点接入指针,指针前移一位
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next
        # 遍历完成后，检查p1, p2是否到达链表尾部
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        
        return dummy.next