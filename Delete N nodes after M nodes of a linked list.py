class Solution:
    def linkdelete(self, head, n, m):
        # Code here
        current = head

        while current:
            for _ in range(m - 1):
                if current is None:
                    return
                current = current.next
            
            if current is None:
                return
            
            temp = current.next
            for _ in range(n):
                if temp is None:
                    break
                temp = temp.next
            
            current.next = temp
            current = temp
