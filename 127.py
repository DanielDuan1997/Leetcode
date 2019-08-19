from collections import defaultdict
from queue import Queue
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
        if endWord not in wordList:
            return 0
        len_begin_word = len(beginWord)
        wordDict = defaultdict(list)
        for word in wordList:
            if len(word) != len_begin_word:
                continue
            for i in range(len_begin_word):
                wordDict[word[:i] + '*' + word[i+1:]].append(word)
        q = Queue()
        q.put((beginWord, 1))
        visited = {beginWord: True}
        while not q.empty():
            item = q.get()
            word = item[0]
            step = item[1]
            for i in range(len_begin_word):
                star_word = word[:i] + '*' + word[i+1:]
                for nxt_word in wordDict[star_word]:
                    if nxt_word == endWord:
                        return step + 1
                    if nxt_word not in visited:
                        visited[nxt_word] = True
                        q.put((nxt_word, step+1))
        return 0
