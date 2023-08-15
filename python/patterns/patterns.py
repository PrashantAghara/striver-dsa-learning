def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()


def pattern2(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end="")
        print()


def pattern3(N):
    for i in range(N):
        for j in range(N - i):
            print("* ", end="")
        print()


def pattern4(N):
    for i in range(N):
        for j in range(N - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        for j in range(N - i - 1):
            print(" ", end="")
        print()


def pattern5(N):
    for i in range(N):
        for j in range(i):
            print(" ", end="")
        for j in range(2 * (N - i - 1) + 1):
            print("*", end="")
        print()


# Print Diamond
def pattern6(N):
    pattern4(N)
    pattern5(N)


# Symmetric Pattern
def pattern7(N):
    for i in range(1, 2 * N):
        stars = i;
        if i > N:
            stars = 2 * N - i
        for j in range(stars):
            print("* ", end="")
        print()
