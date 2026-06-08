#Q. Pattern_1: Implement fibonacchi with memozation.
#T: O(N), S: O(N)
# Without memo, T is 2^N

# Only Returns the Nth fibonacchi number
def fibonacci_memoization(n,memo):
    if(n == 0): return 0
    if(n == 1): return 1
    if(memo[n] != None):
        return memo[n]

    current_result = fibonacci_memoization(n-1,memo) + fibonacci_memoization(n-2,memo)
    memo[n] = current_result
    return current_result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input("Calculate fibonni series for until X: "))
    memo = [None]*(n+1)
    fibonacci_memoization(n, memo)
    for i in range(n+1):
        print(fibonacci_memoization(i, memo))
