def calculate_installment_price(vehicle_price, down_payment_rate, loan_period_years, annual_interest_rate):
    loan_amount = vehicle_price * (1 - down_payment_rate / 100)  # 대출 원금
    monthly_interest_rate = annual_interest_rate / 100 / 12  # 월 별 이자율
    num_of_payments = loan_period_years * 12  # 총 할부 개월 수
    
    # 원리금 균등방식으로 매월 납입할 금액 계산
    monthly_payment = loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -num_of_payments)
    
    total_paid_over_time = monthly_payment * num_of_payments  # 총 상환 금액
    total_interest_paid = total_paid_over_time - loan_amount  # 총 지불 이자
    
    return round(total_interest_paid), round(monthly_payment)


vehicle_price = 50000000  # 자동차 가격
down_payment_percentage = 20  # 선수금 비율 (%)
loan_period_years = 3  # 대출 기간 (년)
annual_interest_rate_percentage = 5.2  # 연이율 (%)

total_interest_paid, monthly_payment_amt = calculate_installment_price(vehicle_price,
                                                                       down_payment_percentage,
                                                                       loan_period_years,
                                                                       annual_interest_rate_percentage)

print(f"총 이자 합계: {total_interest_paid}원")
print(f"한 달 납입금액: {monthly_payment_amt}원")
