def getMinIterations(arr):
    if arr == sorted(arr):
        return True
    insert = 0
    
    while True:
        temp = arr[:-insert if insert != 0 else None]
        # temp2 = arr[:]
        m1 = max(temp)
        temp.remove(m1)
        m2 = max(temp)
        temp.remove(m2)
        temp.append(m1 + m2)
        # arr = temp + arr[len(arr) - 1 - insert:]
        insert += 1
        print(temp)
        break

# print(getMinIterations([1, 3, 3, 4]))
print(getMinIterations([6, 5, 4, 3, 1, 2]))
