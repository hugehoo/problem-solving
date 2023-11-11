def calculate_installment(principal, months, annual_interest_rate):
    monthly_interest_rate = annual_interest_rate / 12 / 100  # 연이율을 월이율로 변환
    installment = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** months / ((1 + monthly_interest_rate) ** months - 1)
    return round(installment)


def formatting(num):
    return format(num, ',d')


원금 = 50_000_000
할부개월 = 36
연금리 = 5.2

월납입금 = calculate_installment(원금, 할부개월, 연금리)

총납입금 = 월납입금 * 할부개월
총이자액 = 총납입금 - 원금


print(f"매달 납입해야할 금액은 {formatting(월납입금)}원 입니다.")
print(f"총 납입해야할 금액은 {formatting(총납입금)}원 입니다.")
print(f"총 이자는 {formatting(총이자액)}원 입니다.")


