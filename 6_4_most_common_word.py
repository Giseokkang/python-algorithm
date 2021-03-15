import re
import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [
            word
            for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
            if word not in banned
        ]
        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]


input = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

s = Solution()
result = s.mostCommonWord(input, banned)
print(result)