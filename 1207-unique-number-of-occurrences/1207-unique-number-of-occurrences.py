class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count = {}
        for num in arr :
            if num in count :
                count[num]+=1
            else:
                count[num]=1
        freq = list(count.values())

        return len(freq)==len(set(freq))