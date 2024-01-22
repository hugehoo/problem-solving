class Solution:
    def reverseWords(self, s: str):
        splitted = s.split(" ")
        result =[split for split in splitted if split != ""]
        answer = [rev for rev in result[::-1]]
        return " ".join(answer)
        