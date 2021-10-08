# your code goes here
def main():
    case = int(input())
    for _ in range(case):
        n, k = input().split(' ')
        n = int(n)
        k = int(k)
        if k == 1:
            return 1

        dp = [0]
        i = 0
        mod = 10**9 + 7
        while True:
            if len(dp) > k:
                break
            N = len(dp)
            for j in range(N):
                dp.append((dp[j] + n ** i) % mod)
            i += 1

        print(dp[k])


if __name__ == '__main__':
    main()
