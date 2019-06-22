from functools import lru_cache
@lru_cache(500000)
def wabbits(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n< 1 :
        return -1
    else:
        return wabbits(n-1, k) + wabbits(n-2, k) + 0*wabbits(n-3, k)
print(wabbits(6,3))
