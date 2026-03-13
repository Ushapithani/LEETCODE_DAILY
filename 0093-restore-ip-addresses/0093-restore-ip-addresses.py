class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []
        
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    for d in range(1, 4):
                        if a + b + c + d == len(s):
                            A = s[:a]
                            B = s[a:a+b]
                            C = s[a+b:a+b+c]
                            D = s[a+b+c:]
                            if all(int(x) <= 255 and str(int(x)) == x 
                                   for x in [A, B, C, D]):
                                result.append(f"{A}.{B}.{C}.{D}")
        return result