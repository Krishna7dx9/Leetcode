class Solution(object):
    def minWindow(self, s, t):

        if len(s) < len(t):
            return ""

        from collections import Counter

        need = Counter(t)
        missing = len(t)

        start = 0
        mini_window = None

        for end in range(len(s)):

            ch = s[end]

            if need[ch] > 0:
                missing -= 1

            need[ch] -= 1

            # shrink when valid
            while missing == 0:

                window_len = end - start + 1
                if mini_window is None or window_len < len(mini_window):
                    mini_window = s[start:end + 1]

                left_char = s[start]
                need[left_char] += 1

                if need[left_char] > 0:
                    missing += 1

                start += 1

        return mini_window if mini_window else ""