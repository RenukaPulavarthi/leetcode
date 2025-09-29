from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        q = deque()
        q.append((beginWord,1))
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        while q:
            curr, steps = q.popleft()
            # print(curr)
            if curr == endWord: return steps
            for i in range(len(curr)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    pre = curr[:i] + j + curr[i+1::]
                    if pre in wordSet:
                        wordSet.remove(pre)
                        q.append((pre,steps + 1))
        return 0
                    

