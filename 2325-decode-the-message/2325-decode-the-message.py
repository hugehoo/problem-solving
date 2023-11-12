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
            # print(k, v)
        result = []
        for m in message:
            if m == " ":
                result.append(" ")
                continue
            result.append(alpha_dict[m])
        
        return "".join(result)