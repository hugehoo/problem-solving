from collections import defaultdict
class Solution:
    def displayTable(self, orders: list[list[str]]) -> list[list[str]]:
        table_set = set()
        menu_set = set()
        menu_dict = defaultdict(list)
        for name, table, menu, in orders:
            menu_set.add(menu)
            table_set.add(table)
            menu_dict[int(table)].append(menu)

        menu_set = sorted(menu_set)
        header = ['Table']
        header = header + list(menu_set)
        result = [header]
        keys = sorted(menu_dict.keys())
        for k in keys:
            semi = [str(k)]
            for h in header[1:len(menu_set) +1]:
                semi.append(str(menu_dict[(k)].count(h)))
            result.append(semi)
        return result