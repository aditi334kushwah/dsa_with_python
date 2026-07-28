class Solution(object):
    def findSubstring(self, s, words):

        if not s or not words:
            return []

        wordLen = len(words[0])
        wordCount = len(words)

        totalLen = wordLen * wordCount

        need = {}

        for word in words:
            need[word] = need.get(word, 0) + 1


        ans = []


        # Try every possible offset
        for offset in range(wordLen):

            left = offset
            right = offset

            window = {}
            count = 0


            while right + wordLen <= len(s):

                word = s[right:right+wordLen]
                right += wordLen


                if word in need:

                    window[word] = window.get(word,0)+1
                    count += 1


                    # Too many same words
                    while window[word] > need[word]:

                        leftWord = s[left:left+wordLen]

                        window[leftWord] -= 1

                        left += wordLen
                        count -= 1


                    # Found valid window
                    if count == wordCount:

                        ans.append(left)


                        # Move window forward
                        leftWord = s[left:left+wordLen]

                        window[leftWord] -= 1

                        left += wordLen
                        count -= 1


                else:

                    # Reset
                    window.clear()
                    count = 0
                    left = right


        return ans