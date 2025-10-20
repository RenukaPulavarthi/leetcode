from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        que = deque()
        wordSet = set(wordList)
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        que.append((beginWord, 1))
        while que:
            curr, steps = que.popleft()
            if curr == endWord:
                return steps
            for i in range(len(curr)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    present = curr[:i] + j + curr[i+1:]
                    if present in wordSet:
                        que.append((present, steps + 1))
                        wordSet.remove(present)
        return 0
