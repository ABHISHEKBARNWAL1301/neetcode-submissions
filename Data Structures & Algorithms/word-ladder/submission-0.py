class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        queue = deque([beginWord])
        ans = 1
        while queue:
            size = len(queue)
            print(queue)
            for _ in range(size):
                word = queue.popleft()
                if word == endWord:
                   return ans
                for i in range(len(word)):
                    for j in range(26):
                        char = word[:i] + chr(ord('a')+j) + word[i+1:]
                        if char in wordList and char != word:
                            queue.append(char)
                            wordList.remove(char)
                
            ans += 1

        return 0