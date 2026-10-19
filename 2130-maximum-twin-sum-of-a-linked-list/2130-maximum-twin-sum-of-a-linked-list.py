class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        mp = {}
        idx = 0
        temp = head
        
        while temp:
            mp[idx] = temp.val
            idx += 1
            temp = temp.next
            
        ans = 0
        for i in range(idx // 2):
            ans = max(ans, mp[i] + mp[idx - 1 - i])
            
        return ans