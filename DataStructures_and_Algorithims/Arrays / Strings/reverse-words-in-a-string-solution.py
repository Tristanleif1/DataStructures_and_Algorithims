class Solution:
    def reverseWords(self, s: str) -> str:
        list_of_chars = s.split()

        reversed_str = list_of_chars[::-1]

        return ' '.join(reversed_str)