def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    name_ranking_one = {}
    for step, name in zip(steps_one, names_one):
        name_ranking_one[name] = max(name_ranking_one.get(name, 0), step)
    
    name_ranking_two = {}
    for step, name in zip(steps_two, names_two):
        name_ranking_two[name] = max(name_ranking_two.get(name, 0), step)
    
    name_ranking_three = {}
    for step, name in zip(steps_three, names_three):
        name_ranking_three[name] = max(name_ranking_three.get(name, 0), step)
    
    final = {}
    for dic in [name_ranking_one, name_ranking_two, name_ranking_three]:
        for k, v in dic.items():
            final[k] = final.get(k, 0) + v
    sorted_dict = dict(sorted(final.items(), key=lambda x: x[1], reverse=True))
    return list(sorted_dict.keys())


print(solution([1, 2, 3], ['james', 'bob', 'alice'], [10, 20, 30], ['james', 'alice', 'bob'], [1000, 1, 1],
               ['bob', 'alice', 'james']))
