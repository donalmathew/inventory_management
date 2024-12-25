import itertools

a="hir"
arr=[]
b=itertools.permutations(a)
for perm in b:
    arr.append(''.join(perm))
print(arr)