import sys


def main():
    n, k = map(int, input().split())
    while k:
        n += (n % 10)
        k -= 1
    print(n)


if __name__ == '__main__':
    main()
