#Dividing circles
def f(n: int) -> int:
    a = 1
    for i in range(2, n+1):
        a *= i
    return a

def c(n: int, p: int) -> int:
    return f(n) // (f(p) * f(n-p))

if __name__ == "__main__":
    n = int(input())
    R = 1 + (((n-1)*n)//2) + (((n) * (n - 1) * (n - 2 ) * (n - 3))//24)
    print(R)
    #print(c(n, 4) + c(n, 2) + 1)
