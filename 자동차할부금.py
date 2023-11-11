def calculate_installment(principal, months, annual_interest_rate):
    monthly_interest_rate = annual_interest_rate / 12 / 100  # 연이율을 월이율로 변환 (퍼센트 표기를 실수로 변환)
    installment = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** months / ((1 + monthly_interest_rate) ** months - 1)
    return round(installment)

principal = float(input("자동차 가격을 입력하세요: ")) - float(input("선납금액을 입력하세요: "))
months = int(input("할부 개월 수를 입력하세요: "))
annual_interest_rate = float(input("연이율(%)를 입력하세요: "))

installment = calculate_installment(principal, months, annual_interest_rate)

total_payment = installment * months
total_interest_payment = total_payment - principal

print(f"매달 납입해야할 금액은 {installment}원 입니다.")
print(f"총 납입해야할 금액은 {total_payment}원 입니다.")
print(f"총 이자는 {total_interest_payment}원 입니다.")
