class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        List = []
        curr = head

        
        while curr:
            List.append(curr.val)
            curr = curr.next

        
        List.sort()

        
        curr = head
        for i in range(len(List)):
            curr.val = List[i]
            curr = curr.next

        return head
