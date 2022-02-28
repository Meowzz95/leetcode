def solve(sample):
    seen = set()
    for c in sample:
        if c in seen:
            return c
        seen.add(c)
    return None

tcs = [
    ["GeeskForGeeks","e"],
    ["hello geeks","l"],
]
for tc in tcs:
    res = solve(tc[0])
    print(res,res==tc[1])