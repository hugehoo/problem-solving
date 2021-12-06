def solution(n, recipes, orders):
    recipe_dict = {}
    for i in recipes:
        a, b = i.split(' ')
        recipe_dict[a] = b
    # n은 가동 가능 화구

    for order in orders:
        print(order.split(' '))  # 숫자는 주문한 시간, cooking time, order time 은 1 초 이상 자연수.


    answer = 0
    return answer


n = 3
recipes = ["SPAGHETTI 3", "FRIEDRICE 2", "PIZZA 8"]
orders = ["PIZZA 1",
          "FRIEDRICE 2",
          "SPAGHETTI 4",
          "SPAGHETTI 6",
          "PIZZA 7",
          "SPAGHETTI 8"]

print(solution(n, recipes, orders))
