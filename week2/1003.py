counts = [0,0]
def fibonaccicount(n):

    if n == 0:
        counts = [1, 0]
        return counts

    elif n == 1:
        counts = [0, 1]
        return counts

    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        counts = [a, b]
        return counts
        
n = int(input())
for i in range(n):
    result = fibonaccicount(int(input()))
    print(result[0], result[1])
