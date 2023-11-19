class Solution:
    def interpret(self, command: str) -> str:
        dict_ = {
            "G": "G",
            "()": "o",
            "(al)": "al"
        }
        command = list(command)
        
        answer = ""
        for idx, c in enumerate(command):
            if c == "(" and command[idx + 1] == ")":
                answer += "o"
            elif c == "G":
                answer += 'G'
            elif c == "(" and command[idx + 1] == "a":
                answer += 'al'
            else:
                continue
        return answer
