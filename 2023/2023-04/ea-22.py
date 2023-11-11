def solution(folders, files, selected, excepted):
    selected_folders = set(selected)
    folder_dict = {parent: set() for _, parent in folders}
    for child, parent in folders:
        folder_dict[parent].add(child)
        if parent in selected_folders:
            selected_folders.add(child)
    
    total_size = 0
    count = 0
    for name, size, folder in files:
        if name not in excepted and folder in selected_folders:
            total_size += convert_to_bytes(size)
            count += 1
    
    return [total_size, count]


def convert_to_bytes(size):
    if size.endswith('KB'):
        return int(size[:-2]) * 1024
    elif size.endswith('B'):
        return int(size[:-1])


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