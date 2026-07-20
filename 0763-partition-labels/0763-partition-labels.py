class Solution(object):
    def partitionLabels(self, s):
        # Store the last occurrence of each character
        last = {}

        for i in range(len(s)):
            last[s[i]] = i

        result = []
        start = 0
        end = 0

        # Traverse the string
        for i in range(len(s)):
            # Update the farthest end of the current partition
            end = max(end, last[s[i]])

            # If we've reached the end of the partition
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result