from typing import List


def merge(l, r):
    res = []
    li = 0
    ri = 0
    while li < len(l) and ri < len(r):
        lv = l[li]
        rv = r[ri]
        if lv < rv:
            res.append(lv)
            li += 1
        else:
            res.append(rv)
            ri += 1

    while li < len(l):
        res.append(l[li])
        li += 1
    while ri < len(r):
        res.append(r[ri])
        ri += 1
    return res


def merge_sort(list: List):
    if len(list) <= 1:
        return list

    mi = len(list) // 2
    l = list[:mi]
    r = list[mi:]

    l = merge_sort(l)
    r = merge_sort(r)

    return merge(l, r)


print(merge_sort([2, 1, 3, 99, 88, 7, 1, 5]))
