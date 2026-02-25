class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def process(string):
            result = ""
            for char in string:
                if char != "#":
                    result += char
                else:
                    result = result[:-1]
            return result

        return process(s) == process(t)