class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        set_list = []
        for k in key:
            if k == " ":
                continue
            if k not in set_list:
                set_list.append(k)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alpha_dict = {}
        for k, v in zip(alphabet, set_list):
            alpha_dict[v] = k
        return "".join([alpha_dict.get(m, " ") for m in message])