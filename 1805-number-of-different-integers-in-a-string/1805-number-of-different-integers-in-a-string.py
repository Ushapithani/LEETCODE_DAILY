class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = ""
        
        for ch in word:
            if ch.isdigit():
                s += ch
            else:
                s += " "
        
        nums = s.split()
        
        st = set()
        for num in nums:
            st.add(num.lstrip('0') or '0')
        
        return len(st)