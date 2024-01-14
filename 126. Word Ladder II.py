from collections import deque

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


class Solution:
    def ladderLength(self, beginWord, endWord, wordList,ans):
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        q = deque()
        q.append((beginWord, 1))

        while q:
            word, step = q.popleft()
            for i in range(len(beginWord)):
                for j in range(26):
                    newWord = word[:i] + chr(97 + j) + word[i + 1:]
                    if newWord == endWord:
                        return step + 1
                    if newWord in wordList:
                        ans.append(newWord)
                        q.append((newWord, step + 1))
                        wordList.remove(newWord)
        return 0

l = Solution()
ans=[]
s= l.ladderLength(beginWord,endWord,wordList,ans)
print(ans)