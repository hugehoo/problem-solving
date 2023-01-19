import re


def check_string(amount_text):
    amount_list = amount_text.split(',')
    filtered = list(filter(lambda x: len(x) != 3, amount_list[1:]))
    if filtered:
        return False
    return True


def solution(amountText):
    answer = True
    pattern = r'^[0-9,]+$'
    if amountText.startswith('0') or amountText.startswith(',') or amountText.endswith(','):
        return False
    if not re.match(pattern, amountText):
        return False
    if not check_string(amountText):
        return False
    return answer


print(solution("39000"))
print(solution("39,000"))
print(solution("39,00"))
