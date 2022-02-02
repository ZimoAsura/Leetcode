# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 利用LC21的思路，两两合并, 直到k个合并完
        # 时间复杂度(NK)
        # 额外空间复杂度O(NK)
        # 这种方法不够好
        if not lists: return None
        res = None
        for i in lists:
            res = self.mergetwo(res, i)
        return res
    
    def mergetwo (self, list1, list2):
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        # 注意虚拟头节点的使用
        p1, p2 = list1, list2
        dummy = ListNode(None)
        p = dummy
        while p1 and p2:
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return dummy.next