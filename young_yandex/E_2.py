import sys


def main():
    n, k = map(int, input().split())
    for item in range(k):
        n += (n % 10)
    print(n)


if __name__ == '__main__':
    main()
