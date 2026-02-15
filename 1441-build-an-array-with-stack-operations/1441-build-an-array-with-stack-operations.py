class Solution:
    def buildArray(self, target, n):
        result = []
        num, i = 1, 0
        while i < len(target):
            if target[i] == num:
                result.append("Push")
                i += 1
            else:
                result.append("Push")
                result.append("Pop")
            num += 1
        return result