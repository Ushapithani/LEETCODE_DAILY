class Solution:
    def uniqueMorseRepresentations(self, words):
        morse_map = {
            'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.",
            'g': "--.", 'h': "....", 'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..",
            'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.",
            's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-",
            'y': "-.--", 'z': "--.."
        }
        
        transformations = set()
        
        for word in words:
            code = ""
            for ch in word:
                code += morse_map[ch]
            transformations.add(code)
        
        return len(transformations)

