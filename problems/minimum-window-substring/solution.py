class Solution(object):
    def minWindow(self, s, t):
        
        mini_window = None
        
        # Early exit using impossible case
        if len(s) < len(t):
            return ""

        # Generating freq_t 
        freq_t = [0] * 52
        for ch in t:
            if 'A' <= ch <= 'Z':
                idx = ord(ch) - ord('A')
            else:
                idx = ord(ch) - ord('a') + 26
            freq_t[idx]  += 1 

        # Generating all substring
        for start in range(len(s)):
            for end in range(start, len(s)):
                substring = s[start: end + 1]
                freq_substring = [0]*52

                # Generating freq for every substring
                for ch in substring:
                    if 'A' <= ch <= 'Z':
                        idx = ord(ch) - ord('A')
                    else:
                        idx = ord(ch) - ord('a') + 26
                    freq_substring[idx] += 1 

                # Checking freq of t in freq_substring
                ok = True
                for i in range(52):
                    if freq_substring[i] < freq_t[i]:
                        ok = False
                        break

                if ok and (mini_window is None or len(substring) < len(mini_window)):
                    mini_window = substring

        return mini_window                    