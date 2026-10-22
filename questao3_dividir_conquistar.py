
def mdc(L, A):
    if A == 0:
        return L
    return mdc(A, L % A)

L = int(input())
A = int(input())

print(mdc(L, A))
