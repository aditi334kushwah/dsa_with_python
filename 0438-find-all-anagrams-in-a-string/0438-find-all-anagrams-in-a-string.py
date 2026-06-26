from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):

        if len(p) > len(s):
            return []

        p_count = Counter(p)
        window = Counter()

        left = 0
        ans = []

        for right in range(len(s)):

            # Add current character
            window[s[right]] += 1

            # Keep window size equal to len(p)
            if right - left + 1 > len(p):

                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

            # Compare frequency maps
            if right - left + 1 == len(p):

                if window == p_count:
                    ans.append(left)

        return ans



            
        