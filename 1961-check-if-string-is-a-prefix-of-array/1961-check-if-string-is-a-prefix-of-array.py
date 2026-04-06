class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        temp = ""
        for word in words:
            temp+=word
            if len(temp)==len(s):
                return temp ==s
            if len(temp)>len(s):
                return False
        return False
        