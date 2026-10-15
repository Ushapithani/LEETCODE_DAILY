
class Solution:
    def reformatNumber(self, number: str) -> str:
        s = ""

        for ch in number:
            if ch.isdigit():
                s += ch

        result = ""

        while len(s) > 4:
            result += s[:3] + "-"
            s = s[3:]

        if len(s) == 4:
            result += s[:2] + "-" + s[2:]
        else:
            result += s

        return result
