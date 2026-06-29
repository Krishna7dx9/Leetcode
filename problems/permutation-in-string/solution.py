class Solution(object):
    def checkInclusion(self, s1, s2):

        freq1 = {}
        freq_substring = {}
        freq_substring[s2[0]] = freq_substring.get(s2[0], 0) + 1
        end = 1

        for ch in s1:
            freq1[ch] = freq1.get(ch, 0) + 1

        for start in range(len(s2) - len(s1) + 1):

            while end <= start + len(s1) - 1:
                freq_substring[s2[end]] = freq_substring.get(s2[end], 0) + 1
                end += 1

            if freq_substring == freq1:
                return True

            freq_substring[s2[start]] -= 1
            if freq_substring[s2[start]] == 0:
                del freq_substring[s2[start]]
        
        return False