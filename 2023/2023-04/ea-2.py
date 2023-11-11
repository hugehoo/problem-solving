from collections import defaultdict
from functools import reduce


def solution(folders, files, selected, excepted):
    # 1 folders 간 관계를 파악해야돼.
    # 하위에 존재하는 걸 set 로  묶자
    # folder_dict
    fd = defaultdict(set)
    for child, parent, in folders:
        fd[parent].add(child)
    
    # 2 selected 순회하며 탐색할 폴더를 정해서 또 set 에 담는다.
    selected_folder = set()
    for s in selected:
        selected_folder.add(s)
        if fd.get(s):
            for element in fd[s]:
                selected_folder.add(element)
        else:
            selected_folder.add(s)
    
    total_size = []
    count = 0
    for name, size, folder, in files:
        if name not in excepted and folder in selected_folder:
            total_size.append(size)
            count += 1
    total_bytes = reduce(lambda x, y: x + y, map(convert_to_bytes, total_size))
    
    return [total_bytes, count]


def convert_to_bytes(item):
    if 'KB' in item:
        return int(item.replace('KB', '')) * 1024
    elif 'B' in item:
        return int(item.replace('B', ''))


print(
    solution([["animal", "root"], ["fruit", "root"]],
             [["cat", "1B", "animal"], ["dog", "2B", "animal"], ["apple", "4B", "fruit"]],
             ["animal"],
             ["apple"])
)

print(
    solution([["food", "root"], ["meat", "food"], ["fruit", "food"], ["animal", "root"]],
             [["cat", "1B", "animal"], ["dog", "2B", "animal"], ["fork", "1KB", "meat"],
              ["beef", "8KB", "meat"], ["apple", "4B", "fruit"], ["fire", "83B", "root"]],
             ["root", "meat"],
             ["fork", "apple"])
)
# [3, 2]
"""
동일한 등차 구간은 제끼고 연산 가능
8000 + 83 + 1 + 2
8086

안녕하세요 혹시 2번 문제-예시 2번의 바이트 총합이 8278B 가 맞나요?
"""
