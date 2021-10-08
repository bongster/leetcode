import math


def main():
    [m, n, a] = [int(i) for i in input().split(" ")]
    ans = math.ceil(m / a) * math.ceil(n / a)
    print(ans)


if __name__ == '__main__':
    main()
