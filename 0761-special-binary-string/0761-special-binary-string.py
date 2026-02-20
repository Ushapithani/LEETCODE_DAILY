class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        specials = []
        
        for j, c in enumerate(s):
            count += 1 if c == '1' else -1
            if count == 0:
                inner = self.makeLargestSpecial(s[i+1:j])
                specials.append('1' + inner + '0')
                i = j + 1
        
        specials.sort(reverse=True)
        return ''.join(specials)