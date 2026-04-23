class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        mid = len(s)//2
        count1=0 
        count2=0
        for i in range(mid):
            if s[i] in vowels:
                count1+=1
        for i in range(mid,len(s)):
            if s[i] in vowels:
                count2+=1
        return count1==count2
        