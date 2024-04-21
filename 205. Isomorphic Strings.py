class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        dict_1 = {}
        dict_2 = {}

        for i in range(n):
            char_s = s[i]
            char_t = t[i]

            if char_s not in dict_1 and char_t not in dict_2:
                dict_1[char_s] = char_t
                dict_2[char_t] = char_s

            elif char_s in dict_1 and dict_1[char_s] != char_t:
                return False

            elif char_t in dict_2 and dict_2[char_t] != char_s:
                return False

        return True
