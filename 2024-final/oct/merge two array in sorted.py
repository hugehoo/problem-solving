# def merge_sorted_arrays(arr1: list[int], arr2: list[int]):
#     merged = []
#     i, j = 0, 0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             merged.append(arr1[i])
#             i += 1
#         else:
#             merged.append(arr2[j])
#             j += 1
#     while i < len(arr1):
#         merged.append(arr1[i])
#         i += 1
#     while j < len(arr2):
#         merged.append(arr2[j])
#         j += 1
#     return merged
#
#
# def merged_two_arrays(arr1, arr2):
#     merged = []
#     i, j = 0, 0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] <= arr2[j]:
#             merged.append(arr1[i])
#             i += 1
#         else:
#             merged.append(arr2[j])
#             j += 1
#     while i < len(arr1):
#         merged.append(arr1[i])
#         i += 1
#     while j < len(arr2):
#         merged.append(arr2[j])
#         j += 1
#     return merged


def merge_sorted_arrays(arr1: list, arr2: list) -> list:
    result = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    if i < len(arr1):
        result.extend(arr1[i:])
    if j < len(arr2):
        result.extend(arr2[j:])
    
    return result


if __name__ == "__main__":
    result = merge_sorted_arrays([1, 3, 5, 8, 10, 11], [2, 4, 5, 7, 8, 9])
    print(result)
    
    # result = merged_two_arrays([1, 3, 5, 8, 10, 11], [2, 4, 5, 7, 8, 9])
    # print(result)
