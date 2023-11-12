class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(" ", "")
        set_list = []
        for k in key:
            if k not in set_list:
                set_list.append(k)

        alpha_dict = {}
        for k, v in zip("abcdefghijklmnopqrstuvwxyz", set_list):
            alpha_dict[v] = k

        return "".join([alpha_dict.get(m, " ") for m in message])


s = Solution()
print(s.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
