class Solution(object):
    def checkInclusion(self, s1, s2):

        if len(s1) > len(s2):
            return False

        end = 1
        matches = 0
        arr1 = [0]*26
        window = [0] *26
        window[ord(s2[0]) - ord('a')] += 1

        for ch in s1:
            arr1[ord(ch) - ord('a')] += 1

        # Build first complete window
        while end <= len(s1) - 1:
            index = ord(s2[end]) - ord('a')
            window[index] += 1
            end += 1

        # Initial matches
        for i in range(26):
            if arr1[i] == window[i]:
                matches += 1

        for start in range(len(s2) - len(s1) + 1):

            if matches == 26:
                return True

            while end <= start + len(s1) - 1:
                index = ord(s2[end]) - ord('a')
                window[index] += 1
                end += 1

                if window[index] == arr1[index]:
                    matches += 1
                elif window[index] == arr1[index] + 1:
                    matches -= 1

            if matches == 26:
                return True

            index = ord(s2[start]) - ord('a')
            window[index] -= 1
        
            if window[index] == arr1[index]:
                matches += 1
            elif window[index] == arr1[index] - 1:
                matches -= 1

        return False