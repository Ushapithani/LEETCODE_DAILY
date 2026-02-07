class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = 0 
        deletions = 0 
        b_count = 0
        for ch in s :
            if ch == 'a':
                deletions = min(deletions +1, b_count)
            elif ch == 'b':
                b_count+=1
        return deletions 
        