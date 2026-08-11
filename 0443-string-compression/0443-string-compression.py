class Solution:
    def compress(self, chars: List[str]) -> int:
        pos = 0
        i = 0

        while i < len(chars):
            ch = chars[i]
            count = 0

            while i < len(chars) and chars[i] == ch:
                i += 1
                count += 1

            chars[pos] = ch
            pos += 1

            if count > 1:
                for x in str(count):
                    chars[pos] = x
                    pos += 1

        return pos