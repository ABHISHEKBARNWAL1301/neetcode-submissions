class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        queue = deque([beginWord])
        words, res = set(wordList), 0

        ans = 1
        while queue:
            res += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                   return res
                for i in range(len(word)):
                    for j in range(26):
                        char = word[:i] + chr(ord('a')+j) + word[i+1:]
                        if char in words and char != word:
                            queue.append(char)
                            words.remove(char)
                

        return 0