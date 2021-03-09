class Solution:
    def reverseString(self, s: list[str]) -> None:
        s[:] = s[::-1]


a = Solution()
print(a.reverseString(["h", "e", "l", "l", "o"]))
