class Solution(object):
    def countVowelSubstrings(self, word):

        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0

        for low in range(len(word)):

            for high in range(low, len(word)):

                v = word[low:high + 1]

                # Substring must contain only vowels
                if any(ch not in vowels for ch in v):
                    break

                # All five vowels should be present
                if len(set(v)) == 5:
                    count += 1

        return count

                    