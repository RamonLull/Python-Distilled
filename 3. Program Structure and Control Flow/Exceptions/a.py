from collections import Counter


def is_valid(s: str) -> bool:
    cnt = Counter(s)
    values = list(cnt.values())
    length = len(set(values))
    if length == 1:
        return True
    else:
        for index, value in enumerate(values):
            if value != values[0]:
                if abs(value - values[0]) > 1:
                    return False
                list1 = values.copy()
                list1[index] = values[0]
                list2 = values.copy()
                list2[0] = value
                if len(set(list1)) == 1 or len(set(list2)) == 1:
                    return True
                else:
                    return False


my_string = input()
print(is_valid(my_string))
